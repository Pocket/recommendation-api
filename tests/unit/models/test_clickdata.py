from app.models.clickdata import ClickdataModel

class TestClickdata:

    def test_dynamodb_row_to_clickdata(self):
        row = {
            "clicks": 0.045687984008122705,
            "created_at": 1610404066,
            "expires_at": 1644359266,
            "impressions": 2.207612237118199,
            "mod_item": "topic/default"
        }

        clickdata = ClickdataModel.dynamodb_row_to_clickdata(row)
        assert clickdata.clicks == 0.045687984008122705
        assert clickdata.impressions == 2.207612237118199
        assert clickdata.mod_item == "topic/default"
