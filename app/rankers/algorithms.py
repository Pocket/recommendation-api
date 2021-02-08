from aws_xray_sdk.core import xray_recorder
from typing import List

from app.models.recommendation import RecommendationModel


def top15(recs: List[RecommendationModel]):
    # TODO: implement
    return recs


def top30(recs: List[RecommendationModel]):
    # TODO: implement
    return recs


def thompson_sampling(recs: List[RecommendationModel]):
    # TODO: implement
    return recs


@xray_recorder.capture('rankers_algorithms_spread_publishers')
def spread_publishers(recs: List[RecommendationModel], spread: int = 3) -> List[RecommendationModel]:
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
