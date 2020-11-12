import logging
import sys
import re

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport


def get_topic_map(endpoint: str = "explore-topics.readitlater.com"):
    query = gql("""
                     query {listTopics {
                                 id
                                 slug
                                 curatorLabel
                                 displayName
                                 query
                                 isDisplayed
                                 pageType
                                 customFeedId
                               }}
                 """)

    sample_transport = RequestsHTTPTransport(
        url=f"https://{endpoint}", verify=True, retries=3,
    )
    client = Client(transport=sample_transport, fetch_schema_from_transport=True)
    result = client.execute(query)
    topic_map = dict()
    for hit in result["listTopics"]:
        key = re.sub("[- ]", "_", hit["slug"])  # legacy key for topic_map from json
        topic_map[key] = hit

    return topic_map


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


def convert_to_days(scale: str) -> str:
    """
    convert time window string from weeks to days as needed for ES queries
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


def _check_timescale(qstr: str, splitter: str = "w"):
    """
    this routine checks to see if timescale is in weeks
    :param qstr: the timescale string
    :param splitter: "w" splits on weeks
    :return: boolean indicating if timescale is in units determined by qstr
    """
    return qstr.partition(splitter)[0].isdigit() and qstr.partition(splitter)[1] == splitter

