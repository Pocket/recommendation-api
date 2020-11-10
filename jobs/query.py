
from elasticsearch_dsl.query import Bool, MultiMatch
from elasticsearch_dsl.query import Exists, Range, Term, Match
from typing import Dict, Optional, List
from dataclasses import dataclass

from utils import convert_to_days, publisher_spread_reranking


@dataclass
class ItemRec:
    item_id: int  # Identifier for the item being recommended
    feed_id: Optional[int]  # Optionally specify feed to show curated metadata in UI

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
        for i in range(len(source["approved_feeds"])):
            # if feed_id is set, pay attention to that feed only for approval time
            if feed_id and source["approved_feeds"][i]["approved_feed_id"] == feed_id:
                time_live = source["approved_feeds"][i]["approved_feed_time_live"]
                feed_id_used = feed_id
                break
            else:  # get most recent approval time
                if not time_live or time_live > source["approved_feeds"][i]["approved_feed_time_live"]:
                    time_live = source["approved_feeds"][i]["approved_feed_time_live"]
                    feed_id_used = source["approved_feeds"][i]["approved_feed_id"]

        rec_approval_times.append((r, time_live, feed_id_used))

    return sorted(rec_approval_times, key=lambda x: x[1], reverse=True)


def transform_curated_results(raw_results: Dict, feed_id: int = 1) -> List:
    """
    This routine takes the raw elastic search output and converts to a List of ItemRecs
    ordered by time_approved
    :param raw_results: elastic search results output
    :param curated: boolean flag indicating if results are curated recs
    :return: dict with specified algorithmic and curated fields, only one will be populated
    """

    sorted_recs = order_curated_by_approval_time(raw_results, feed_id)
    out = list()
    for hit in sorted_recs:
        source = hit[0]["_source"]
        out.append({"item_id": source["resolved_id"], "feed_id": feed_id})

    return out


def merge_collection_results(results1: Dict, feed_id1: int, results2: Dict, feed_id2) -> List:
    """
    This routine takes the raw elastic search output and converts to a List of ItemRecs
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
        out.append({"item_id": source["resolved_id"], "feed_id": hit[2]})

    return out


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
