from elasticsearch_dsl.query import Bool, MultiMatch
from elasticsearch_dsl.query import Exists, Range, Term, Match
from elasticsearch_dsl.function import Gauss, FieldValueFactor
from typing import Dict, List

from utils import convert_to_days

FEED_ID_EN_US = 1

def order_curated_by_approval_time(raw_results: Dict, feed_id: int = None) -> List:
    """
    This orders curated recommendations by time approved accounting for multiple runs
    in different curated feeds
    :param raw_results:
    :param feed_id:
    :return:
    """

    recs = [x for x in raw_results["hits"]["hits"]]
    rec_approval_times = list()
    for r in recs:
        source = r["_source"]
        time_live = None
        feed_id_used = None
        for feed in source["approved_feeds"]:
            # if feed_id is set, pay attention to that feed only for approval time
            if feed_id and feed["approved_feed_id"] == feed_id:
                time_live = feed["approved_feed_time_live"]
                feed_id_used = feed_id
                break
            else:  # otherwise get most recent approval time
                if not time_live or time_live > feed["approved_feed_time_live"]:
                    time_live = feed["approved_feed_time_live"]
                    feed_id_used = feed["approved_feed_id"]

        rec_approval_times.append((r, time_live, feed_id_used))

    return sorted(rec_approval_times, key=lambda x: x[1], reverse=True)


def transform_curated_results(raw_results: Dict, feed_id: int = FEED_ID_EN_US) -> List:
    """
    This routine takes the raw elastic search output and converts to a List of items
    ordered by time_approved
    :param raw_results: elastic search results output
    :param feed_id: curated feed_id
    :return: dict with specified algorithmic and curated fields, only one will be populated
    """

    sorted_recs = order_curated_by_approval_time(raw_results, feed_id)
    out = list()
    for hit in sorted_recs:
        source = hit[0]["_source"]
        out.append({"item_id": source["resolved_id"], "publisher": source["domain"]["top_domain_name"],
                    "feed_id": feed_id})

    return out


def merge_collection_results(results1: Dict, feed_id1: int, results2: Dict, feed_id2) -> List:
    """
    This routine takes the raw elastic search output and converts to a List of items
    sorted by time approved by curator
    :param results1: elastic search results from curator label query
    :param feed_id1: feed_id for curation of results 1
    :param results2: elastic search results from feed_id query
    :param feed_id2: feed_id for curation of results 2
    :return: dict with specified algorithmic and curated fields, only one will be populated
    """

    sorted_items_times1 = order_curated_by_approval_time(results1, feed_id1)
    sorted_items_times2 = order_curated_by_approval_time(results2, feed_id2)

    # tuples here are (rec, approval_time, feed_id)
    all_items_times = sorted_items_times1 + sorted_items_times2
    all_items_times = sorted(all_items_times, key=lambda x: x[1], reverse=True)

    out = list()
    for hit in all_items_times:
        source = hit[0]["_source"]
        out.append({"item_id": source["resolved_id"], "publisher": source["domain"]["top_domain_name"],
                    "feed_id": hit[2]})

    return out


def postprocess_search_results(raw_results, allowlist, limit):
    """
    * filter results that are not from publishers included in allowlist
    * retain fields required for ranking
    :param raw_results: raw elastic search results
    :param allowlist: domain allowlist
    :param limit: desired number of returned results
    :return: list of recs with reduced fields
    """
    recs = [x for x in raw_results["hits"]["hits"]]
    filtered = list()
    for r in recs:
        source = r["_source"]
        if source["domain"]["top_domain_name"] not in allowlist:
            continue

        # recommendations need titles
        if "title" not in source:
            continue

        # collect google category information
        gdata = dict()
        if "google_categories" in source:
            for this in source["google_categories"]:
                gdata[this["google_category"]] = float(this["google_category_score"])

        approved_feed_id = None
        if "approved_feeds" in source:
            if FEED_ID_EN_US in [x["approved_feed_id"] for x in source["approved_feeds"]]:
                approved_feed_id = FEED_ID_EN_US  # assuming en-US is what matters for the API

        filtered.append({"rec": {"item_id": source["resolved_id"],
                                 "top_domain_name": source["domain"]["top_domain_name"],
                                 "title": source["title"],
                                 "feed_id": approved_feed_id,
                                 "google_categories": gdata},
                         "es_score": r["_score"]})

    return filtered[:limit]


def organic_by_topic(curator_topic: str, topic_map: Dict,
                     scale: str = "90d", feed: int = FEED_ID_EN_US) -> Bool:
    """
    routine for item search by topic from organic curated recs
        - default ordering by publication date
    :param curator_topic: topic string must be a curator topic
    :param topic_map: topic map with additional info
    :param scale: optional time scale for maximum item age
    :param feed: optional feed_id for item filtering by curator feed
    :return: boolean query object
    """

    scale2 = "now-%s" % convert_to_days(scale)
    bool_query = Bool(must=[Range(approved_feeds__approved_feed_time_live={"gte": scale2})])

    # there is something tricky about a term query on a nested field.
    # need to use a match query and treat it like text
    q_topic = topic_map[curator_topic]["curatorLabel"]
    bool_query.must.append(Match(curated_topics__curated_topic_name={"query": q_topic}))
    bool_query.must.append(Match(approved_feeds__approved_feed_id={"query": str(feed)}))

    return bool_query


def collection_by_feed(feed: int, scale: str = "90d") -> Bool:
    """
    routine for item search of organic curated recs for editorial collection based on
    either or both
        - a custom feed_id to grab items
    :param feed: optional feed_id for item filtering by curator feed
    :param scale: optional time scale for maximum item age
    :return: boolean query object
    """

    # get results with specified feed_id
    scale2 = "now-%s" % convert_to_days(scale)
    bool_query = Bool(must=[Range(approved_feeds__approved_feed_time_live={"gte": scale2})])
    bool_query.must.append(Match(approved_feeds__approved_feed_id={"query": str(feed)}))

    return bool_query


def algorithmic_by_topic(curator_topic: str, topic_map: Dict, min_saves: int = 45,
                         scale: str = "90d", save_origin: int = 6000, save_scale: int = 3000):
    """
    routine to generate algorithmic elasticsearch query
    :param curator_topic: topic string must be a curator topic
    :param topic_map: topic map with additional info
    :param min_saves: minimum required number of saves
    :param scale: optional time scale for maximum item age
    :param save_origin: origin in gaussian decay term in fcn score query
    :param save_scale: scale in gaussian decay term in fcn score query
    :return: Bool query
    """

    query_in = topic_map[curator_topic]["query"]

    bool_query = Bool(must=[Exists(field="date_published.date_published_parsed"),
                            Exists(field="date_published.time_first_parsed"),
                            Exists(field="domain.domain_id"),
                            Exists(field="action_counts.save_count"),
                            Exists(field="impact_scores.total_score"),
                            Term(lang="en"),
                            Range(action_counts__save_count={"gte": min_saves})],
                      must_not=[Exists(field="flags")])  # flags are adult or sensitive subjects

    scale2 = convert_to_days(scale) if scale else "180d"
    date_range = "now-%s" % scale2
    bool_query.must.append(Range(date_published__time_first_parsed={"gte": date_range}))

    kw_query = [MultiMatch(query=query_in,
                           type="best_fields",
                           fields=["title^3",
                                   "excerpt"]),
                MultiMatch(query=query_in,
                           boost=2.5,
                           type="best_fields",
                           fields=["google_categories.google_category",
                                   "meta_opengraph_tags.meta_opengraph_tag"])
                ]

    score_functions = [Gauss(date_published__time_first_parsed={
                                "origin": "now",
                                "scale": scale2
                                },
                             ),
                       Gauss(date_published__date_published_parsed={
                                "origin": "now",
                                "scale": scale2
                                },
                             ),
                       FieldValueFactor(field="impact_scores.total_score"),
                       Gauss(action_counts__save_count={
                                "origin": save_origin,
                                "scale": save_scale
                                }, weight=3)]

    return Bool(filter=bool_query, should=kw_query), score_functions
