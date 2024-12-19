import json
import logging
from typing import Dict, Any

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event: Dict[str, Any], context=None):
    """
    Handles SQS messages triggered by REMOVE_ITEM EventBridge events.
    :param event: Event with one or multiple 'Records', where each record's 'body' contains the event payload.
    :param context: Context provided by AWS Lambda, unused in this function.
    """
    records = event['Records']

    for record in records:
        event_body = json.loads(record['body'])
        logger.info("Processing REMOVE_ITEM event: %s", json.dumps(event_body, indent=2))

    return {
        'message': f'Processed {len(records)} records.'
    }
