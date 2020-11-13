from typing import Any, Dict, Union, List
from uuid import UUID
from metaflow import Flow, namespace, metadata
from aws_secretsmanager_caching import SecretCache, InjectKeywordedSecretString
import json
import boto3
import uuid
from datetime import datetime
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from aws_lambda.config.index import sentry, secrets, dynamodb as dynamodb_config, topic_types

sentry_sdk.init(
    dsn=sentry.get('dsn'),
    integrations=[AwsLambdaIntegration()],
    release=sentry.get('release'),
    environment=sentry.get('environment')
)

cache = SecretCache()


def handler(event: Dict[str, Any], context):
    flow_name = get_flow_name(event)
    data = get_metaflow_data(flow_name)
    try:
        dynamodb_batch_write(data, flow_name)
    except Exception as e:
        details = {
            'flow_name': flow_name,
            'run_id': get_run_id(event),
            'data': data,
            'exception': e
        }
        print(f'Insert failed. Details: {details}')
        raise


def dynamodb_batch_write(data, flow_name):
    dynamodb = boto3.resource('dynamodb', endpoint_url=dynamodb_config.get('endpoint_url'))
    table = dynamodb.Table(dynamodb_config.get('explore_topics_candidates_table'))
    with table.batch_writer() as batch:
        for value in data:
            batch.put_item(Item=get_dynamodb_item(value, flow_name))


def get_dynamodb_item(data: Dict, flow_name: str) -> Dict[str, Union[Union[UUID, str], Any]]:
    return {
        'id': str(uuid.uuid4()),
        'topic_id': data['topic_id'],
        'topic_id-type': str(data['topic_id']) + '|' + get_candidate_type(flow_name),
        'created_at': get_current_date_formatted(),
        'candidates': data['items']
    }


def get_candidate_type(flow_name: str) -> str:
    return topic_types.get(flow_name, 'collection')


def get_current_date_formatted() -> str:
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def get_run_id(event: Dict[str, Any]):
    return get_output_params(event)['metaflow.run_id']


def get_flow_name(event: Dict[str, Any]):
    return get_output_params(event)['metaflow.flow_name']


def get_output_params(event: Dict[str, Any]):
    return json.loads(event['detail']['output'])['Parameters']


def get_metaflow_data(flow_name) -> List[Dict[str, Union[int, List[Dict[str, int]]]]]:
    metadata(get_service_url())
    namespace(get_tag())
    flow = Flow(flow_name)
    data = flow.latest_successful_run.data
    return data.results


def get_service_url() -> str:
    return get_json_key_secret_value(secret_id=secrets['metaflow'], json_key='METAFLOW_SERVICE_INTERNAL_URL')


def get_tag() -> str:
    return get_json_key_secret_value(secret_id=secrets['metaflow'], json_key='METAFLOW_DEPLOY_TAG')


# Because of https://github.com/aws/aws-secretsmanager-caching-python/pull/17 we can not use function decorators
def get_json_key_secret_value(secret_id: str, json_key: str):
    # Copied from
    # https://github.com/aws/aws-secretsmanager-caching-python/blob/master/src/aws_secretsmanager_caching/decorators.py#L76
    try:
        secret = json.loads(cache.get_secret_string(secret_id=secret_id))
        return secret[json_key]
    except json.decoder.JSONDecodeError:
        raise RuntimeError('Cached secret is not valid JSON')
