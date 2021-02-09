import json
from typing import List, Dict, Any

import boto3

from aws_lambda.config.index import dynamodb as dynamodb_config


def handler(event: Dict[str, Any], context=None):
    records = event['Records']

    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config.get('endpoint_url'))
    table = dynamodb.Table(dynamodb_config.get('recommendation_api_candidate_sets_table'))
    with table.batch_writer() as batch:
        for record in records:
            candidate_set = json.loads(record['body'])
            batch.put_item(Item=candidate_set)
