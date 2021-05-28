import logging
import json
from typing import Any, Dict, List, Union

from aws_xray_sdk.core import xray_recorder
from app.models.metrics.metrics_model import MetricsModel
from operator import itemgetter
from scipy.stats import beta

from app.config import ROOT_DIR

RankableListType = List[Union['SlateModel', 'RecommendationModel']]
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


def blocklist(recs: RecommendationListType, blocklist: List[str] = None) -> RecommendationListType:
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


DEFAULT_ALPHA_PRIOR = 0.02
DEFAULT_BETA_PRIOR = 1.0


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

    alpha_prior, beta_prior = DEFAULT_ALPHA_PRIOR, DEFAULT_BETA_PRIOR
    if metrics and 'default' in metrics:
        # 'default' is a special key we can use for anything that is missing.
        # The values here aren't actually clicks or impressions,
        # but instead direct alpha and beta parameters for the module CTR prior
        alpha_prior = metrics['default'].training_7_day_opens
        beta_prior = metrics['default'].training_7_day_impressions
        if alpha_prior < 0 or beta_prior < 0:
            logging.error(
                f"Alpha {alpha_prior} or Beta {beta_prior} prior < 0 for module {metrics['default'].id}")
            alpha_prior, beta_prior = DEFAULT_ALPHA_PRIOR, DEFAULT_BETA_PRIOR

    scores = []
    # create prior distribution for CTR from parameters in click data table
    prior = beta(alpha_prior, beta_prior)
    for rec in recs:
        try:
            # Recommendation is keyed on item_id.
            clickdata_id = rec.item.item_id
        except AttributeError:
            # Slates are keyed on their id.
            clickdata_id = rec.id

        d = metrics.get(clickdata_id)
        if d:
            # TODO: Decide how many days we want to look back.
            clicks = max(d.training_7_day_opens + alpha_prior, 1e-18)
            # posterior combines click data with prior (also a beta distribution)
            no_clicks = max(d.training_7_day_impressions - d.training_7_day_opens + beta_prior, 1e-18)
            # sample from posterior for CTR given click data
            score = beta.rvs(clicks, no_clicks)
            scores.append((rec, score))
        else:  # no click data, sample from module prior
            scores.append((rec, prior.rvs()))

    scores.sort(key=itemgetter(1), reverse=True)
    return [x[0] for x in scores]


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
