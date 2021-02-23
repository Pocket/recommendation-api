import sys, os, base64, datetime, hashlib, hmac
import requests
import json
from typing import *
import time

def handler(event, context):
    table = 'RECAPI-Dev-CandidateSets'
    cs_id = '117e17b3-23cc-4343-91d7-2e1a37da78b0'
    region = 'us-east-1'
    endpoint = f'https://dynamodb.{region}.amazonaws.com/'
    #endpoint = 'recapi-dev-mathijs.n7e2yl.clustercfg.dax.use1.cache.amazonaws.com:8111'
    iterations = 100

    result = query(endpoint, region, table, cs_id, 'id', iterations=iterations)
    print(result)

# based on the example python code found here:
# https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html

# call this method to query all items for a given primary hash key in a table
# endpoint: the DynamoDB endpoint to query (for AWS servers, this is "https://dynamodb.{region}.amazonaws.com/")
# region: the AWS region in which the table resides
# table_name: the name of the table to query
# client_name: the value of the primary hash key from which to query items
# hash_key: the name of the primary hash key
# hash_key_type: the type of the primary hash key (the default "S" is "string")
def query(
    endpoint, region, table_name, client_name, hash_key, hash_key_type="S",
iterations=100):
    # collect required authorisation information from the environment
    access_key = os.environ.get("AWS_ACCESS_KEY_ID")
    secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    session_token = os.environ.get("AWS_SESSION_TOKEN")
    more = True
    start_key = None
    results = []
    session = requests.session()

    # continue to send requests until the query is complete
    while more:
        parameters = create_body(table_name, client_name, hash_key, start_key)
        test_start = time.perf_counter()
        for _ in range(iterations):
            response = session.post(
                endpoint,
                data=parameters,
                headers=create_headers(
                    region,
                    parameters,
                    access_key=access_key,
                    secret_key=secret_key,
                    session_token=session_token,
                ),
            )
        test_end = time.perf_counter()
        print(f"Total time: {test_end - test_start:.4f} sec. Average time: "
              f"{(test_end - test_start)/iterations}.")

        # if the query is finished, this key will not be included in the response
        data = response.json()
        try:
            start_key = data["LastEvaluatedKey"]
        except KeyError:
            more = False
        try:
            results += data["Items"]
        except KeyError:
            if response.status_code == 400:
                raise Exception(
                    "Failed to resolve query. It's likely your AWS session token has expired."
                )
            else:
                raise Exception(
                    "Failed to resolve query: received status code "
                    + response.status_code
                )
    return [
        {key: deserialize(value, float) for key, value in item.items()}
        for item in results
    ]


def create_body(
    table_name, client_name, hash_key, start_key=None, hash_key_type="S",
):
    params_dict = {
        "TableName": table_name,
        "KeyConditionExpression": "#n0 = :v0",
        "ExpressionAttributeNames": {"#n0": hash_key},
        "ExpressionAttributeValues": {":v0": {hash_key_type: client_name}},
    }
    if start_key:
        params_dict["ExclusiveStartKey"] = start_key

    request_parameters = json.dumps(params_dict)
    return request_parameters


def create_headers(
    region, request_parameters, access_key=None, secret_key=None, session_token=None
):

    if access_key is None or secret_key is None:
        print("No access key is available.")
        sys.exit()

    service = "dynamodb"
    host = f"dynamodb.{region}.amazonaws.com"
    content_type = "application/x-amz-json-1.0"
    amz_target = "DynamoDB_20120810.Query"
    method = "POST"

    # Create a date for headers and the credential string
    t = datetime.datetime.utcnow()
    amz_date = t.strftime("%Y%m%dT%H%M%SZ")
    date_stamp = t.strftime("%Y%m%d")

    canonical_uri = "/"
    canonical_querystring = ""
    canonical_headers = f"content-type:{content_type}\nhost:{host}\nx-amz-date:{amz_date}\nx-amz-target:{amz_target}\n"

    signed_headers = "content-type;host;x-amz-date;x-amz-target"
    payload_hash = hashlib.sha256(request_parameters.encode("utf-8")).hexdigest()
    canonical_request = f"{method}\n{canonical_uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}"

    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = f"{date_stamp}/{region}/{service}/aws4_request"
    request_digest = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
    string_to_sign = f"{algorithm}\n{amz_date}\n{credential_scope}\n{request_digest}"

    signing_key = getSignatureKey(secret_key, date_stamp, region, service)
    signature = hmac.new(
        signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256
    ).hexdigest()
    authorization_header = f"{algorithm} Credential={access_key}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}"

    # the security token header needs to be included for sessions
    headers = {
        "Content-Type": content_type,
        "X-Amz-Date": amz_date,
        "X-Amz-Target": amz_target,
        "Authorization": authorization_header,
        "X-Amz-Security-Token": session_token,
    }
    return headers


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def getSignatureKey(key, date_stamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), date_stamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning


SIMPLE_TYPES = frozenset({"BOOL", "S", "B"})
SIMPLE_SET_TYPES = frozenset({"SS", "BS"})
NULL_TYPE = "NULL"


def deserialize(value: Dict[str, Any], numeric_type: Callable[[str], Any]) -> Any:
    if not value:
        raise TypeError(
            "Value must be a nonempty dictionary whose key " "is a valid dynamodb type."
        )
    tag, val = next(iter(value.items()))
    if tag in SIMPLE_TYPES:
        return val
    if tag == NULL_TYPE:
        return None
    if tag == "N":
        return numeric_type(val)
    if tag in SIMPLE_SET_TYPES:
        return set(val)
    if tag == "NS":
        return {numeric_type(v) for v in val}
    if tag == "L":
        return [deserialize(v, numeric_type) for v in val]
    if tag == "M":
        return {k: deserialize(v, numeric_type) for k, v in val.items()}
    raise TypeError(f"Dynamodb type {tag} is not supported")
