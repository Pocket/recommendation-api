import json
import time
from copy import deepcopy
from aws_lambda.sqs_handler import MINIMUM_EXPIRES_AT_FROM_NOW


body = {
  "id": "1234-5678-ABCD-CEDF",
  "version": 1,
  "expires_at": int(time.time() + MINIMUM_EXPIRES_AT_FROM_NOW + 3600),  # Expires 1 hour after minimum
  "candidates": [
    {
      "item_id": 3242933715,
      "publisher": "TheAtlantic",
      "feed_id": 1,
    }
  ]
}

body2 = deepcopy(body)
body2['id'] = '2345-5678-ABCD-FDEC'

event = {
  "Records": [
    {
      "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
      "receiptHandle": "MessageReceiptHandle",
      "body": json.dumps(body),
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1523232000000",
        "SenderId": "123456789012",
        "ApproximateFirstReceiveTimestamp": "1523232000001"
      },
      "messageAttributes": {},
      "md5OfBody": "{{{md5_of_body}}}",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
      "awsRegion": "us-east-1"
    },
    {
      "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
      "receiptHandle": "MessageReceiptHandle",
      "body": json.dumps(body2),
      "attributes": {
        "ApproximateReceiveCount": "1",
        "SentTimestamp": "1523232000000",
        "SenderId": "123456789012",
        "ApproximateFirstReceiveTimestamp": "1523232000001"
      },
      "messageAttributes": {},
      "md5OfBody": "{{{md5_of_body}}}",
      "eventSource": "aws:sqs",
      "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
      "awsRegion": "us-east-1"
    }
  ]
}
