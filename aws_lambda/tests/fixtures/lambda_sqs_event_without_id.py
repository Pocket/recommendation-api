import json
from copy import deepcopy

from aws_lambda.tests.fixtures.lambda_sqs_event import body, event


body_without_id = body.copy()
del body_without_id['id']

event_without_id = deepcopy(event)
event_without_id["Records"][0]["body"] = json.dumps(body_without_id)
