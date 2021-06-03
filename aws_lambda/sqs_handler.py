import json
import logging
import time
from typing import Dict, Any

import boto3
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from aws_lambda.config.index import sentry, dynamodb as dynamodb_config

sentry_sdk.init(
    dsn=sentry.get('dsn'),
    integrations=[AwsLambdaIntegration()],
    release=sentry.get('release'),
    environment=sentry.get('environment')
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

MINIMUM_EXPIRES_AT_FROM_NOW = 3600  # expires_at cannot be less that this many seconds from now.


def handler(event: Dict[str, Any], context=None):
    """
    Handles SQS message containing a candidate set.
    :param event: Event with one or multiple 'Records', where each record has a 'body' is a json-encoded candidate set.
    :param context: Currently unused parameter, but required to be specified here, because it's set by Lambda.
    :return:
    """
    records = event['Records']

    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config.get('endpoint_url'))
    table = dynamodb.Table(dynamodb_config.get('recommendation_api_candidate_sets_table'))
    with table.batch_writer() as batch:
        for record in records:
            candidate_set = json.loads(record['body'])
            sentry_sdk.set_context('candidate_set',
                                   {
                                       'id': candidate_set.get('id'),
                                       'flow': candidate_set.get('flow'),
                                       'run': candidate_set.get('run'),
                                   })
            batch.put_item(Item=get_dynamodb_item(candidate_set))

    return {
        'message': f'Processed {len(records)} records.'
    }


def get_dynamodb_item(candidate_set: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates candidate_set and returns item that can be inserted into DynamoDB
    :param candidate_set: Candidate set dict. Will be modified by this method.
    :return:
    """
    logger.info("Validating %s from %s/%s", candidate_set.get("id"), candidate_set.get("flow"), candidate_set.get("run"))
    _validate_candidate_set(candidate_set)

    candidate_set['created_at'] = int(time.time())

    return candidate_set


def _validate_candidate_set(candidate_set: Dict[str, Any]):
    _validate_dict_value_type(candidate_set, 'id', str)
    _validate_dict_value_type(candidate_set, 'version', int)
    _validate_dict_value_type(candidate_set, 'candidates', list)
    _validate_dict_value_type(candidate_set, 'expires_at', int)

    # Check that expires_at is greater than now, such that the item doesn't get deleted immediately.
    min_expires_at = time.time() + MINIMUM_EXPIRES_AT_FROM_NOW
    assert candidate_set['expires_at'] >= min_expires_at,\
        f"expires_at {candidate_set['expires_at']} should be at least {min_expires_at} in {candidate_set}"

    for candidate in candidate_set['candidates']:
        _validate_candidate(candidate)


def _validate_candidate(candidate: Dict[str, Any]):
    _validate_dict_value_type(candidate, 'item_id', int)
    _validate_dict_value_type(candidate, 'publisher', str)


def _validate_dict_value_type(d: Dict, key: str, expected_type: type):
    assert key in d and type(d[key]) == expected_type, f"{key} is not an {expected_type} in {d}"
