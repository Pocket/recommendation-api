
from elasticsearch_dsl.query import Bool, MultiMatch
from elasticsearch_dsl.query import Exists, Range, Term, Match
from typing import Dict, NamedTuple, Optional, List

from jobs.utils import get_feed_item_ids, convert_to_days, publisher_spread_reranking


class ItemRec(NamedTuple):
    feed_item_id: str  # Set to “{rec_src}/{item_id}”. Used by clients and analytics.
    item_id: int  # Identifier for the item being recommended
    feed_id: Optional[int]  # Optionally specify feed to show curated metadata in UI
    rec_src: str  # Identifier of recommendation source: “ExploreTopicRecs”


def transform_results(raw_results: Dict, curated: bool = False) -> Dict:
    """
    This routine takes the raw elastic search output and converts to a List of ItemRecs
    :param raw_results: elastic search results output
    :param curated: boolean flag indicating if results are curated recs
    :return: dict with specified algorithmic and curated fields, only one will be populated
    """

    rec_src = "ExploreTopicAlgorithmic"
    approved_feed_id = None
    if curated:
        source = raw_results["hits"]["hits"][0]["_source"]
        if "approved_feeds" in source:
            approved_feed_id = source["approved_feeds"][0]["approved_feed_id"]
            rec_src = "ExploreTopicCurated"

    out = list()
    for hit in raw_results["hits"]["hits"]:
        source = hit["_source"]
        rec = ItemRec(item_id=source["resolved_id"],
                      rec_src=rec_src,
                      feed_id=approved_feed_id,
                      feed_item_id="/".join([rec_src, str(source["resolved_id"])]))

        out.append(rec._asdict())

    if curated:
        return {"algorithmic_recommendations": [], "curated_recommendations": out}
    else:
        return {"algorithmic_recommendations": out, "curated_recommendations": []}


def merge_collection_results(results1: Dict, results2: Dict) -> Dict:
    """
    This routine takes the raw elastic search output and converts to a List of ItemRecs
    sorted by time approved by curator
    :param results1: elastic search results from curator label query
    :param raw_results: elastic search results from feed_id query
    :return: dict with specified algorithmic and curated fields, only one will be populated
    """


    out = list()

    recs = [x for x in results1["hits"]["hits"]] + [x for x in results2["hits"]["hits"]]
    all_results = sorted(recs, key=lambda x: x["_source"]["approved_feeds"][0]["approved_feed_time_approved"],
                         reverse=True)

    rec_src = "ExploreCollectionCurated"
    for hit in all_results:
        source = hit["_source"]
        approved_feed_id = source["approved_feeds"][0]["approved_feed_id"]
        rec = ItemRec(item_id=source["resolved_id"],
                      rec_src=rec_src,
                      feed_id=approved_feed_id,
                      feed_item_id="/".join([rec_src, str(source["resolved_id"])]))
        out.append(rec._asdict())

    return {"algorithmic_recommendations": [], "curated_recommendations": out}


def organic_by_topic(curator_topic: str, topic_map: Dict,
                     scale: str = "90d", feed: int = 1) -> Bool:
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
    q_topic = topic_map[curator_topic]["curator_label"]
    bool_query.must.append(Match(curated_topics__curated_topic_name={"query": q_topic}))
    bool_query.must.append(Match(approved_feeds__approved_feed_id={"query": str(feed)}))

    return bool_query

def collection_by_feed(feed: int, scale: str = "90d") -> Bool:
    """
    routine for item search of organic curated recs for editorial collection based on
    either or both
        - a custom feed_id to grab items
        - a custom curator label and feed_id = 1 (global-en-US)
    :param feed: optional feed_id for item filtering by curator feed
    :param scale: optional time scale for maximum item age
    :return: boolean query object
    """

    # get results with specified feed_id
    scale2 = "now-%s" % convert_to_days(scale)
    bool_query = Bool(must=[Range(approved_feeds__approved_feed_time_live={"gte": scale2})])
    bool_query.must.append(Match(approved_feeds__approved_feed_id={"query": str(feed)}))

    return bool_query

