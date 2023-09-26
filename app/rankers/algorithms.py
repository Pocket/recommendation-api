from copy import copy
from functools import partial
import logging
import json

from app.models.corpus_item_model import CorpusItemModel
from app.models.metrics.corpus_item_engagement_model import CorpusItemEngagementModel
from app.models.metrics.metrics_model import MetricsModel

from app.config import ROOT_DIR
from typing import List, Dict, Optional, Union
from operator import itemgetter
from scipy.stats import beta

from app.models.slate_config import SlateConfigModel
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
        metrics: Dict[(int or str), Union['MetricsModel', 'CorpusItemEngagementModel']],
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


def boost_syndicated(
        recs: CorpusItemListType,
        metrics: Dict[(int or str), 'CorpusItemEngagementModel'],
        impression_cap: int = 3000000,
        boostable_slot: int = 1,
):
    """
    Boost a syndicated article with fewer than `impression_cap` impressions into `boostable_slot`.
    Requirements and experiment results: https://docs.google.com/document/d/1Vgq63DZQF-pz7R3kvcNXgkUd1I829FZqkIUlpIVY_g4

    :param recs: List of CorpusItem. `url` attribute is used to determine whether a CorpusItem is syndicated.
    :param metrics: Engagement keyed on CorpusItem.id.
    :param impression_cap: Syndicated articles need to have fewer than this many impressions to qualify. Defaults to 3M.
                           See above Google Doc for more details on this threshold.
    :param boostable_slot: 0-based slot to boost an item into. Defaults to slot 1, which is the second recommendation.
    """
    boostable_rec = next(
        (
            r for r in recs[boostable_slot + 1:]
            if r.is_syndicated and (r.id not in metrics or metrics[r.id].trailing_1_day_impressions < impression_cap)
        ), None)
    if boostable_rec:
        recs = copy(recs)  # Don't change the input
        recs.remove(boostable_rec)
        recs.insert(boostable_slot, boostable_rec)

    return recs
