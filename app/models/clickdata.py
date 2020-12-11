from pydantic import BaseModel
from aws_xray_sdk.core import xray_recorder
from typing import List, Dict
from enum import Enum
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.models import Model
from app.config import dynamodb as dynamodb_config


class RecommendationModules(Enum):
    HOME = 'home'
    TOPIC = 'topic'


class ClickdataModel(BaseModel):
    mod_item: str = None
    clicks: int = None
    impressions: int = None
    created_at: int = None
    expires_at: int = None

    @staticmethod
    def dynamodb_row_to_clickdata(row: Dict):
        clickdata = ClickdataModel().parse_obj(row)
        clickdata.item_id = clickdata.mod_item.split("/")[1]
        return clickdata

    @staticmethod
    @xray_recorder.capture_async('model_recommendations_get_recommendations')
    async def get_clickdata(module: RecommendationModules, item_list: List[str]) -> Dict[str, 'ClickdataModel']:

        db = DynamoDBClickData(dynamodb_config["explore_clickdata_table"])
        return db.batch_get(module, item_list)


# this for pynamodb -- i am not sure how to convert this to a pydantic model
class ClickData(Model):
    class Meta:
        pass

    mod_item = UnicodeAttribute(hash_key=True)
    clicks = NumberAttribute()
    impressions = NumberAttribute()
    created_at = NumberAttribute()
    expires_at = NumberAttribute()


def make_key(module: RecommendationModules, key: str):
    return "%s/%s" % (module, key)


class DynamoDBClickData:
    """Live clickdata backed by DynamodB."""

    MOST_RECENT_TIMESTAMP = "most_recent"
    DEFAULT_EXPIRY_S = 15 * 60  # By default expire in 15 minutes
    MIN_EXPIRY_S = 5 * 60  # The smallest number of seconds we will expire in

    def __init__(self, table_name: str, host=None, dynamo=None):
        """Inits DynamoDBClickData class.
        Arguments:
            table_name: Name of the DynamoDB table to reference.
            host: Host override. Used when testing against a local DynamoDB instance.
            dynamo: ClickData object to handle access to Dynamo. Used for testing.
        Raises:
            RuntimeError: If the table doesn't exist
            """
        self.table_name = table_name
        self.dynamo = dynamo or ClickData
        self.dynamo.Meta.table_name = self.table_name

        self.host = host
        if self.host:
            self.dynamo.Meta.host = self.host

        if not self.dynamo.exists():
            raise RuntimeError("Clickdata table (%s) doesn't exist" % table_name)

    def batch_get(self, module: RecommendationModules, items: List[str]) -> Dict:
        """Fetches clickdata for a list of resolved_ids for a given module.
        Args:
            module: Name of the module to fetch data for. These are defined in the OpenAPI spec.
            items: List of resolved_ids to fetch.
        Returns:
            A dict mapping resolved_ids to a `ClickData` model. Note that this function will also always include the
            'default' values for a given module. These aren't click and impression counts, but rather direct alpha and
            beta values that define the Beta distribution that was fit against the module level data.
            This means r['default'].clicks will be the alpha parameter, and r['default'].impressions the beta.
            """
        result = {}

        # Key are namespaced by the module we are getting data from
        keys = {make_key(module, item) for item in items}

        # Always get the default key, it is used for items that don't have any clickstream data
        keys.add(make_key(module, 'default'))

        # Fetch the keys
        found_keys = set()
        for item in self.dynamo.batch_get(keys):
            resolved_id = item.mod_item.split("/")[-1]

            found_keys.add(item.mod_item)
            result[resolved_id] = ClickdataModel(mod_item=item.mod_item,
                                                 clicks=item.clicks,
                                                 impressions=item.impressions,
                                                 created_at=item.created_at,
                                                 expires_at=item.expires_at)

        if not result:
            raise ValueError("No results from DynamoDB. module %s" % module)

        return result

    def __str__(self):
        return "<DynamoDBClickData table_name=%s host=%s>" % (self.table_name, self.host)


class MockData:
    def __init__(self, mod_item, clicks, impressions, created_at, expires_at):
        self.mod_item = mod_item
        self.clicks = clicks
        self.impressions = impressions
        self.created_at = created_at
        self.expires_at = expires_at


class MockClickData:
    def __init__(self, table_name, alpha=0.420, beta=6.257):
        self.alpha = alpha
        self.beta = beta
        self.table_name = table_name

    def batch_get(self, module, items: List[str]) -> Dict:
        return {item: MockData(make_key(module, item), self.alpha, self.beta, 0, 0) for item in
                items + ['default']}

    def __str__(self):
        return "<MockClickData table_name=%s alpha=%s beta=%s>" % (self.table_name, self.alpha, self.beta)
