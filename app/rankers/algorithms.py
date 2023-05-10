from collections import defaultdict
from copy import copy
from functools import partial
import logging
import json
import random

from app.models.corpus_item_model import CorpusItemModel
from app.models.metrics.corpus_item_engagement_model import CorpusItemEngagementModel
from app.models.metrics.metrics_model import MetricsModel
from app.models.metrics.firefox_new_tab_metrics_model import FirefoxNewTabMetricsModel

from app.config import ROOT_DIR
from typing import List, Dict, Optional, Union, Set
from operator import itemgetter
from scipy.stats import beta

from app.models.slate_config import SlateConfigModel
from app.models.personalized_topic_list import PersonalizedTopicList
from app.models.topic import TopicModel

DEFAULT_ALPHA_PRIOR = 0.02
DEFAULT_BETA_PRIOR = 1.0

# These values were taken from: https://github.com/Pocket/feed-machine/blob/master/resources/models/b-0085-15k-age-05-syn-score-explore-locales-rr.json#L4-L5
# They were experimentally derived in 2018: https://getpocket.atlassian.net/browse/P18-616
DEFAULT_FIREFOX_BETA_PRIOR = 15600
DEFAULT_FIREFOX_ALPHA_PRIOR = int(0.0085 * DEFAULT_FIREFOX_BETA_PRIOR)

RankableListType = Union[List['SlateConfigModel'], List['RecommendationModel'], List['CorpusItem']]
RecommendationListType = List['RecommendationModel']
CorpusItemListType = List[CorpusItemModel]


def top_n(n: int, items: RankableListType) -> RankableListType:
    """
    Gets the first n recommendations from the list of recommendations.

    :param items: a list of recommendations in the desired order (pre-publisher spread)
    :param n: The number of items to return
    :return: first n recommendations from the list of recommendations
    """
    if len(items) <= n:
        logging.warning(f"less items than n: {len(items) =} <= {n =} ")

    return items[:n]


top5 = partial(top_n, 5)
top15 = partial(top_n, 15)
top30 = partial(top_n, 30)
top45 = partial(top_n, 45)


def rank_topics(slates: List['SlateConfigModel'], personalized_topics: PersonalizedTopicList) -> List[
    'SlateConfigModel']:
    """
    returns the lineup with topic slates sorted by the user's profile.
    :param slates: initial list of slate configs
    :param personalized_topics: recit response including sorted list of personalized topics
    :return: list of slate configs the personalized topics sorted
    """

    return __personalize_topic_slates(slates, personalized_topics, topic_limit=None)


def top1_topics(slates: List['SlateConfigModel'], personalized_topics: PersonalizedTopicList) -> List[
    'SlateConfigModel']:
    """
    returns the lineup with only the top topic slate included
    :param slates: initial list of slate configs
    :param personalized_topics: recit response including sorted list of personalized topics
    :return: list of slate configs with only the top topic slate
    """

    return __personalize_topic_slates(slates, personalized_topics, topic_limit=1)


def top3_topics(slates: List['SlateConfigModel'], personalized_topics: PersonalizedTopicList) -> List[
    'SlateConfigModel']:
    """
    returns the lineup with only the top 3 topic slates included
    :param slates: initial list of slate configs
    :param personalized_topics: recit response including sorted list of personalized topics
    :return: list of slate configs with only the top 3 topic slate
    """

    return __personalize_topic_slates(slates, personalized_topics, topic_limit=3)


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
        metrics: Dict[(int or str), Union['MetricsModel', 'FirefoxNewTabMetricsModel', 'CorpusItemEngagementModel']],
        trailing_period: int = 28,
        default_alpha_prior=DEFAULT_ALPHA_PRIOR,
        default_beta_prior=DEFAULT_BETA_PRIOR) -> RankableListType:
    """
    Re-rank items using Thompson sampling which combines exploitation of known item CTR
    with exploration of new items with unknown CTR modeled by a prior

    Thompson Sampling uses click data to make a list of tried-and-true recommendations that typically generate a
    lot of interest, mixed in with some newer ones that we want to try out so we can keep adding more interesting
    items to our repertoire.

    :param recs: a list of recommendations in the desired order (pre-publisher spread)
    :param metrics: a dict with item_id as key and dynamodb row modeled as ClickDataModel
    :param trailing_period: the number of days that impressions and opens are aggregated for sampling
    :return: a re-ordered version of recs satisfying the spread as best as possible
    """

    # if there are no recommendations, we done
    if not recs:
        return recs

    opens_column = f"trailing_{trailing_period}_day_opens"
    imprs_column = f"trailing_{trailing_period}_day_impressions"

    if any(not (hasattr(m, opens_column) and hasattr(m, opens_column)) for m in metrics.values()):
        raise ValueError(f"Missing attribute {opens_column} or {imprs_column} on some metrics: {metrics.values()}")

    # Currently we are using the hardcoded priors below.
    # TODO: We should return to having slate/lineup-specific priors. We could load slate-priors from
    #  MODELD-Prod-SlateMetrics, although that might require an additional database lookup. We might choose to use a
    #  'default' key that aggregates engagement data in the same table, such that no additional lookups are required.
    alpha_prior, beta_prior = default_alpha_prior, default_beta_prior

    scores = []
    # create prior distribution for CTR from parameters in click data table
    prior = beta(alpha_prior, beta_prior)
    for rec in recs:
        # When metrics data no longer keyed on item_id, we can simple do `metrics_model = metrics.get(rec.id)`.
        if rec.id in metrics:
            metrics_model = metrics[rec.id]
        else:
            try:
                # Legacy recommendations are keyed on item_id.  Note that the metrics model grabs the item_id
                # when it parses the clickdata by splitting the primary key in dynamo.
                metrics_model = metrics.get(rec.item.item_id, None)
            except AttributeError:
                metrics_model = None

        if metrics_model:
            open_metric = getattr(metrics_model, opens_column)
            imprs_metric = getattr(metrics_model, imprs_column)

            opens = max(open_metric + alpha_prior, 1e-18)
            # posterior combines click data with prior (also a beta distribution)
            no_opens = max(imprs_metric - open_metric + beta_prior, 1e-18)
            # sample from posterior for CTR given click data
            score = beta.rvs(opens, no_opens)
            scores.append((rec, score))

            if hasattr(rec, 'ranked_with_engagement_updated_at') and hasattr(metrics_model, 'updated_at'):
                rec.ranked_with_engagement_updated_at = metrics_model.updated_at
        else:  # no click data, sample from module prior
            scores.append((rec, prior.rvs()))

    scores.sort(key=itemgetter(1), reverse=True)
    return [x[0] for x in scores]


thompson_sampling_1day = partial(thompson_sampling, trailing_period=1)
thompson_sampling_7day = partial(thompson_sampling, trailing_period=7)
thompson_sampling_14day = partial(thompson_sampling, trailing_period=14)
thompson_sampling_28day = partial(thompson_sampling, trailing_period=28)

firefox_thompson_sampling_1day = partial(
    thompson_sampling,
    trailing_period=1,
    default_alpha_prior=DEFAULT_FIREFOX_ALPHA_PRIOR,
    default_beta_prior=DEFAULT_FIREFOX_BETA_PRIOR,
)


def __personalize_topic_slates(input_slate_configs: List['SlateConfigModel'],
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
            if topic_limit:
                if added_topic_slates < topic_limit:
                    output_configs.append(personalizable_configs[personalized_index])
                    added_topic_slates += 1
                    personalized_index += 1
            else:
                output_configs.append(personalizable_configs[personalized_index])
                personalized_index += 1
                added_topic_slates += 1
        else:
            logging.debug(f"adding topic slate {added_topic_slates}")
            output_configs.append(config)

    return output_configs


def rank_by_impression_caps(
        recs: CorpusItemListType,
        user_impression_capped_list: List[CorpusItemModel],
) -> CorpusItemListType:
    """
    removes items that a user has already seen too many times or saw too many days previous

    :param recs:
    :param user_impression_capped_list a list of CorpusItem ids loaded from the feature store per user
    :return: ranked list of recs for the user
    """
    capped_corpus_item_ids = {c.id for c in user_impression_capped_list}
    return [r for r in recs if r.id not in capped_corpus_item_ids] + \
           [r for r in recs if r.id in capped_corpus_item_ids]


def rank_by_preferred_topics(
        recs: CorpusItemListType,
        preferred_topics: List[TopicModel]
) -> CorpusItemListType:
    """
    Boosts preferred topics to the top.

    :param recs: candidates
    :param preferred_topics: List of topics that the user has expressed a preference for.
    :return: ordered list of recommendations with preferred topics.
    """
    preferred_corpus_topic_ids = {t.corpus_topic_id for t in preferred_topics}
    return [r for r in recs if r.topic in preferred_corpus_topic_ids] + \
           [r for r in recs if r.topic not in preferred_corpus_topic_ids]


def spread_attribute(
        recs: Union[CorpusItemListType, RecommendationListType],
        name: str,
        spread_distance: int = None
) -> Union[CorpusItemListType, RecommendationListType]:
    """
    :param recs: The recommendations to be spread
    :param name: The attribute name to be spread on. All recs should have this attribute.
    :param spread_distance: The distance that recs with the same attribute value should be spread apart. The default
        value of None greedily maximizes the distance, by basing the spread distance on the number of unique values.
    :return: Recommendations spread by an attribute, while otherwise preserving the order.
    """
    if spread_distance is None:
        spread_distance = len(set(getattr(r, name) for r in recs)) - 1
    result_recs = []
    remaining_recs = copy(recs)

    while remaining_recs:
        values_to_avoid = set(getattr(r, name) for r in result_recs[-spread_distance:])
        # Get the first remaining rec which value should not be avoided, or default to the first remaining rec.
        rec = next((r for r in remaining_recs if getattr(r, name) not in values_to_avoid), remaining_recs[0])
        result_recs.append(rec)
        remaining_recs.remove(rec)

    return result_recs


spread_topics = partial(spread_attribute, name='topic')
spread_publishers = partial(spread_attribute, name='publisher', spread_distance=3)


def unique_domains_first(recs: List) -> List:
    """
    Reranks a list of recommendations to put items with unique domains to the beginning of the list
    
    :param recs: a list of objects with attribute 'domain' ranked by a recommender
    :return: a re-ordered version of recs 
    """
    seen_domains = set()
    duplicates = []
    uniques = []
    for r in recs:
        if r.domain not in seen_domains:
            uniques.append(r)
            seen_domains.add(r.domain)
        else:
            duplicates.append(r)
    return uniques + duplicates
