import json
import http.client
import urllib.parse
from aws_synthetics.selenium import synthetics_webdriver as syn_webdriver
from aws_synthetics.common import synthetics_logger as logger


def verify_request(method, url, post_data=None, headers={}):
    parsed_url = urllib.parse.urlparse(url)
    user_agent = str(syn_webdriver.get_canary_user_agent_string())
    if "User-Agent" in headers:
        headers["User-Agent"] = f"{user_agent} {headers['User-Agent']}"
    else:
        headers["User-Agent"] = user_agent

    logger.info(f"Making request with Method: '{method}' URL: {url}: Data: {json.dumps(post_data)} Headers: {json.dumps(headers)}")

    if parsed_url.scheme == "https":
        conn = http.client.HTTPSConnection(parsed_url.hostname, parsed_url.port)
    else:
        conn = http.client.HTTPConnection(parsed_url.hostname, parsed_url.port)

    conn.request(method, url, post_data, headers)
    response = conn.getresponse()
    logger.info(f"Status Code: {response.status}")
    logger.info(f"Response Headers: {json.dumps(response.headers.as_string())}")

    if not response.status or response.status < 200 or response.status > 299:
        try:
            logger.error(f"Response: {response.read().decode()}")
        finally:
            if response.reason:
                conn.close()
                raise Exception(f"Failed: {response.reason}")
            else:
                conn.close()
                raise Exception(f"Failed with status code: {response.status}")

    logger.info(f"Response: {response.read().decode()}")
    logger.info("HTTP request successfully executed.")
    conn.close()


def main():
    url = 'https://recommendation-api.readitlater.com'
    method = 'POST'
    post_data = "{\n    \"query\": \"query SyntheticNewTabSlate($locale: String!, $region: String, $count: Int) { newTabSlate(locale: $locale, region: $region) { id recommendations(count: $count) { id tileId corpusItem { id } } }}\",\n    \"variables\": {\"locale\": \"en-US\", \"region\": \"US\", \"count\": 50},\n    \"operationName\": \"SyntheticNewTabSlate\"\n}"
    headers = {"apollographql-client-name":"my-synthetic-api-monitor","apollographql-client-version":"123","Content-Type":"application/json"}

    verify_request(method, url, post_data, headers)

    logger.info("Canary successfully executed.")


def handler(event, context):
    logger.info("Selenium Python API canary.")
    main()