import json
import unittest

from app.models.slate_config import SlateConfigModel


class TestSlateConfigLoadFromJson(unittest.TestCase):
    def test_load_from_json(self):
        json_str = """
        {
            "id": "c410516f-18b3-46a1-b356-c7c003de2b53",
            "displayName": "Trending Articles",
            "description": "Curated articles",
            "experiments": [
             {
               "description": "TS window 30",
               "candidateSets": [
                 "39d0dc54-f6f8-4f13-bea4-4320b3bd8217",
                 "df8a86c1-8b40-48bf-b85d-c144ed96c3fc"
               ],
               "rankers": [
                 "top30",
                 "thompson-sampling",
                 "pubspread"
               ]
             },
             {
               "description": "TS window 15",
               "candidateSets": [
                 "39d0dc54-f6f8-4f13-bea4-4320b3bd8217",
                 "df8a86c1-8b40-48bf-b85d-c144ed96c3fc"
               ],
               "rankers": [
                 "top15",
                 "thompson-sampling",
                 "pubspread"
               ],
               "weight": 0.5
             }
            ]
        }
        """
        slateconfig = SlateConfigModel.load_from_dict(json.loads(json_str))
        self.assertEqual(slateconfig.id, "c410516f-18b3-46a1-b356-c7c003de2b53")
        self.assertEqual(slateconfig.description, "Curated articles")
        self.assertEqual(slateconfig.displayName, "Trending Articles")
