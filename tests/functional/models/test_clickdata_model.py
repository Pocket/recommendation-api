from tests.functional.test_dynamodb_base import TestDynamoDBBase
from app.models.clickdata import ClickdataModel, RecommendationModules


class TestClickdataModel(TestDynamoDBBase):

    def test_get_clickdata_by_item(self):
        self.clickdataTable.put_item(Item={
            "mod_item": "home/999999",
            "clicks": "99",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/666666",
            "clicks": "66",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        self.clickdataTable.put_item(Item={
            "mod_item": "home/333333",
            "clicks": "33",
            "impressions": "999",
            "created_at": "0",
            "expires_at": "0"
        })

        executed = ClickdataModel.get_clickdata(RecommendationModules.HOME, ["666666", "333333"])
        assert len(executed) == 2
        assert "666666" in executed
        assert "333333" in executed
        assert "999999" not in executed
