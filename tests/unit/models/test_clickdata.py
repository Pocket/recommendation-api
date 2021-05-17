from decimal import Decimal

from app.models.clickdata.recommendation_clickdata_model import RecommendationClickdataModel


class TestClickdata:

    def test_dynamodb_row_to_clickdata(self):
        row = {
            "clicks": Decimal(0.045687984008122705),
            "created_at": Decimal(1610404066),
            "expires_at": Decimal(1644359266),
            "impressions": Decimal(2.207612237118199),
            "mod_item": "topic/default",
        }

        clickdata = RecommendationClickdataModel.parse_obj(row)
        assert clickdata.clicks == 0.045687984008122705
        assert clickdata.impressions == 2.207612237118199
        assert clickdata.mod_item == "topic/default"
