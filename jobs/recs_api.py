import logging
import re

from requests import HTTPError
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

def get_topic_map(endpoint: str = "recommendation-api.readitlater.com"):
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
    try:
        client = Client(transport=sample_transport, fetch_schema_from_transport=True)
    except HTTPError:
        logging.error("Failed to establish graphql client to get topic_map")

    result = client.execute(query)
    topic_map = dict()
    for hit in result["listTopics"]:
        key = re.sub("[- ]", "_", hit["slug"])  # legacy key for topic_map from json
        topic_map[key] = hit

    return topic_map
