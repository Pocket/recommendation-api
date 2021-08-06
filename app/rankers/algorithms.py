import logging
import json

from aws_xray_sdk.core import xray_recorder
from app.models.metrics.metrics_model import MetricsModel

from app.config import ROOT_DIR
from typing import List, Dict, Optional, Union
from operator import itemgetter
from scipy.stats import beta

from app.models.slate_config import SlateConfigModel
from app.models.personalized_topic_list import PersonalizedTopicList

DEFAULT_ALPHA_PRIOR = 0.02
DEFAULT_BETA_PRIOR = 1.0

RankableListType = Union[List['SlateModel'], List['RecommendationModel']]
RecommendationListType = List['RecommendationModel']


def top5(items: RankableListType) -> RankableListType:
    """
    Gets the first 5 recommendations from the list of recommendations.

    :param items: a list of recommendations in the desired order (pre-publisher spread)
    :return: first 5 recommendations from the list of recommendations
    """
    return items[:5]


def top15(items: RankableListType) -> RankableListType:
    """
    Gets the first 15 recommendations from the list of recommendations.

    :param items: a list of recommendations in the desired order (pre-publisher spread)
    :return: first 15 recommendations from the list of recommendations
    """
    return items[:15]


def top30(items: RankableListType) -> RankableListType:
    """
    Gets the first 30 recommendations from the list of recommendations.

    :param items: a list of recommendations in the desired order (pre-publisher spread)
    :return: first 30 recommendations from the list of recommendations
    """
    return items[:30]


def top45(items: RankableListType) -> RankableListType:
    """
    Gets the first N recommendations from the list of recommendations.

    :param items: a list of recommendations in the desired order (pre-publisher spread)
    :param n: int, number of recommendations to be returned
    :return: first n recommendations from the list of recommendations
    """
    return items[:45]


def blocklist(recs: RecommendationListType, blocklist: Optional[List[str]] = None) -> RecommendationListType:
    """
    this filters recommendations by item_id using the blocklist available
    in ./app/resources/blocklists.json
    :param recs: a list of recommendations in the desired order (pre-publisher spread)
    :param blocklist: a list of item_ids to be blocked
    :return: filtered recommendations from the input list of recommendations
    """
    if not blocklist:
        with open(ROOT_DIR + "/app/resources/blocklists.json", "r") as fp:
            blocklists = json.load(fp)
        return [rec for rec in recs if str(rec.item.item_id) not in blocklists["items"]]
    else:
        return [rec for rec in recs if rec.item.item_id not in blocklist]


def thompson_sampling(
        recs: RankableListType,
        metrics: Dict[(int or str), 'MetricsModel']) -> RankableListType:
    """
    Re-rank items using Thompson sampling which combines exploitation of known item CTR
    with exploration of new items with unknown CTR modeled by a prior

    Thompson Sampling uses click data to make a list of tried-and-true recommendations that typically generate a
    lot of interest, mixed in with some newer ones that we want to try out so we can keep adding more interesting
    items to our repertoire.

    :param recs: a list of recommendations in the desired order (pre-publisher spread)
    :param metrics: a dict with item_id as key and dynamodb row modeled as ClickDataModel
    :return: a re-ordered version of recs satisfying the spread as best as possible
    """

    # if there are no recommendations, we done
    if not recs:
        return recs

    # Currently we are using the hardcoded priors below.
    # TODO: We should return to having slate/lineup-specific priors. We could load slate-priors from
    #  MODELD-Prod-SlateMetrics, although that might require an additional database lookup. We might choose to use a
    #  'default' key that aggregates engagement data in the same table, such that no additional lookups are required.
    alpha_prior, beta_prior = DEFAULT_ALPHA_PRIOR, DEFAULT_BETA_PRIOR

    scores = []
    # create prior distribution for CTR from parameters in click data table
    prior = beta(alpha_prior, beta_prior)
    for rec in recs:
        try:
            # Recommendations are keyed on item_id.  Note that the metrics model grabs the item_id
            # when it parses the clickdata by splitting the primary key in dynamo
            clickdata_id = rec.item.item_id
        except AttributeError:
            # Slates are keyed on their slate id, in this case the id field of the slate config model
            # Similarly these are parsed as the prefix of the primary key in the slate metrics table
            clickdata_id = rec.id

        d = metrics.get(clickdata_id)
        if d:
            # TODO: Decide how many days we want to look back.
            clicks = max(d.trailing_28_day_opens + alpha_prior, 1e-18)
            # posterior combines click data with prior (also a beta distribution)
            no_clicks = max(d.trailing_28_day_impressions - d.trailing_28_day_opens + beta_prior, 1e-18)
            # sample from posterior for CTR given click data
            score = beta.rvs(clicks, no_clicks)
            scores.append((rec, score))
        else:  # no click data, sample from module prior
            scores.append((rec, prior.rvs()))

    scores.sort(key=itemgetter(1), reverse=True)
    return [x[0] for x in scores]


def personalize_topic_slates(input_slate_configs: List['SlateConfigModel'],
                             personalized_topics: PersonalizedTopicList,
                             topic_limit: Optional[int] = 1) -> List['SlateConfigModel']:
    """
    This routine takes a list of slates as input in which must include slates with an associated curator topic
    label.  It uses the topic_profile that is supplied by RecIt to re-rank the slates according to affinity
    with items in the user's list.
    This version allows non-topic slates within the lineup.  These are left in order in the output configs
    list.  Personalizable (topic) slates are re-ordered using their initial slots in the config lineup.
    If the topic_limit parameter is included this will determine the number of topic slates that
    remain in the output config list.
    :param input_slate_configs: SlateConfigModel list that includes slates with curatorTopicLabels
    :param personalized_topics: response from RecIt listing topics ordered by affinity to user
    :param topic_limit: desired number of topics to return, if this is set the number of slates returned is truncated.
                        otherwise all personalized topics among the input slate configs are returned
    :return: SlateLineupExperimentModel with reordered slates
    """
    topic_to_score_map = {t.curator_topic_label: t.score for t in personalized_topics.curator_topics}
    # filter non-topic slates
    personalizable_configs = list(filter(lambda s: s.curator_topic_label in topic_to_score_map, input_slate_configs))
    logging.debug(personalizable_configs)

    if not personalizable_configs:
        raise ValueError(f"Input lineup to personalize_topic_slates includes no topic slates")
    elif topic_limit and len(personalizable_configs) < topic_limit:
        raise ValueError(f"Input lineup to personalize_topic_slates includes fewer topic slates than requested")

    # re-rank topic slates
    personalizable_configs.sort(key=lambda s: topic_to_score_map.get(s.curator_topic_label), reverse=True)

    output_configs = list()
    added_topic_slates = 0
    personalized_index = 0
    for config in input_slate_configs:
        if config in personalizable_configs:
            # if slate is personalizable add highest ranked slate remaining
            if added_topic_slates < topic_limit:
                output_configs.append(personalizable_configs[personalized_index])
                added_topic_slates += 1
                personalized_index += 1
        else:
            logging.debug(f"adding topic slate {added_topic_slates}")
            output_configs.append(config)

    return output_configs


@xray_recorder.capture('rankers_algorithms_spread_publishers')
def spread_publishers(recs: RecommendationListType, spread: int = 3) -> RecommendationListType:
    """
    Makes sure stories from the same publisher/domain are not listed sequentially, and have a configurable number
    of stories in-between them.

    :param recs: a list of recommendations in the desired order (pre-publisher spread)
    :param spread: the minimum number of items before we can repeat a publisher/domain
    :return: a re-ordered version of recs satisfying the spread as best as possible
    """

    # if there are no recommendations, we done
    if not len(recs):
        return recs

    # move first item in list to first item in re-ordered list
    reordered = [recs.pop(0)]

    # iterator to keep track of spread between domains
    iterator = 0

    # iterate over remaining items in recs
    while len(recs):
        # if there aren't enough items left in recs to satisfy the desired domain spread,
        # or if the iterator reaches the end of recs, then we cannot spread any further.
        # just add the rest of the recs as-is to the end of the re-ordered list.

        # note that this is a simplistic take - we could write more logic here to decrease the spread value by
        # one each time if iterator reaches or exceeds the length of recs
        if (len(recs) <= spread) or (iterator >= len(recs)):
            reordered.extend(recs)
            break

        # get a list of domains that are currently invalid in the sequence
        if len(reordered) > spread:
            # if we have enough items in the reordered list, the invalid domains are the last spread number
            domains_to_check = [x.publisher for x in reordered[-spread:]]
        else:
            # if we don't have more than spread items reordered, just get all the domains in reordered
            domains_to_check = [x.publisher for x in reordered]

        # we can add the rec at iterator position to the re-ordered list if.the rec at iterator has a different
        # domain than the invalid list retrieved above
        if recs[iterator].publisher not in domains_to_check:
            reordered.append(recs.pop(iterator))
            iterator = 0
        else:
            # if we cannot add the rec at position iterator to the re-ordered list, increment the iterator and try
            # the next item in recs
            iterator += 1

    return reordered
