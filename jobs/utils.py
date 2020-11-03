import collections
import logging
import sys
import numpy as np
from typing import Dict
from uuid import uuid4


def setup_logger():
    root = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(
        logging.Formatter(
            '{ "time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message": %(message)s }'
        )
    )
    root.setLevel(logging.DEBUG)
    root.addHandler(ch)


def get_feed_item_ids(entries):
    if len(entries) == 0:
        return[]
    for entry in entries:
        if entry['post_id'] != 0:
            suffix = "p%s" % (str(hex(entry['post_id']))[2:])
        else:
            suffix = "r%s" % (str(hex(entry['resolved_id']))[2:])
        entry['feed_item_id'] = "%s-%s" % (uuid4(), suffix)
    return entries


def convert_to_days(scale: str) -> str:
    """
    convert time window string from weeks to days
    :param scale: input time window string in days or weeks
    :return: time window string in days
    """
    if _check_timescale(scale, 'w'):
        scale2 = '%dd' % (int(scale.partition('w')[0]) * 7)
    elif _check_timescale(scale, 'd'):
        scale2 = scale
    else:
        raise ('{} is not a valid time range'.format(scale))
    return scale2


def _check_timescale(qstr: str, splitter: str):
    return qstr.partition(splitter)[0].isdigit() and qstr.partition(splitter)[1] == splitter


def publisher_spread_reranking(input_recs: Dict, min_spacing: int = 3, max_items: int = 5) -> Dict:
    """
    greedy routine to space out items recommended per publisher
    such that items from the same publisher are separated by
    min_space other items
    :param input_recs: initial list of recommendations
    :param min_spacing: integer gap between items from the same publisher
    :param max_items: integer maximum number of items from the same publisher
    :return:
    """

    results = {"_stats": input_recs["_stats"]}
    nhits = len(input_recs["result"])
    doc_scores = np.zeros(nhits)
    pub_count = collections.Counter()
    # combination of approval model, topic prediction, and search relevance
    # topic weights will be absent for non-topic i.e. search queries
    # approval score is scaled by search relevance in _approval_reranking
    for i, hit in enumerate(input_recs["result"]):
        doc_scores[i] = hit["final_score"]
    # scale to [0, 1]
    doc_scores -= np.min(doc_scores)
    doc_scores /= np.max(doc_scores)
    candidates = set(range(nhits))
    g = np.zeros(nhits)
    rlist, last_publishers = list(), list()
    # goal is to rank by descending doc_score while keeping min_spacing items
    # between any two items from the same publisher
    while (len(rlist) < nhits) and candidates:
        g.fill(-1.0)  # all valid candidates have non-negative scores
        c = np.fromiter(candidates, dtype=int)
        g[c] = doc_scores[c]
        # find best scoring item, rec_star and its index, g_star
        g_star = int(np.argmax(g))
        rec_star = input_recs["result"][g_star]
        max_score = g[g_star]
        # check if its domain is among previous min_spacing items list, last_publishers
        while rec_star["top_domain_name"] in last_publishers and max_score >= 0:
            g[g_star] = -1.0
            g_star = int(np.argmax(g))
            rec_star = input_recs["result"][g_star]
            max_score = g[g_star]
        if max_score >= 0:
            rec_star["model_rank"] = g_star
            rec_star["pub_rerank"] = len(rlist)
            pub_star = rec_star["top_domain_name"]
            rlist.append(rec_star)
            pub_count[pub_star] += 1
            # append newly added item's domain to last_publishers
            if len(last_publishers) <= min_spacing:
                last_publishers.append(pub_star)
            # pop oldest item's domain from last_publishers
            if len(last_publishers) > min_spacing:
                last_publishers.pop(0)
            # last candidate has score 0, others may have -1 if they violate spacing
            candidates.remove(g_star)
            if pub_count[pub_star] == max_items:
                pub_items = set([x for x in candidates if input_recs["result"][x]["top_domain_name"] == pub_star])
                candidates = candidates.difference(pub_items)
        else:
            rlist.extend([input_recs["result"][i] for i in candidates])
            break

    results["result"] = rlist
    return results

