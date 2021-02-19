import unittest

from app.models.slate_config import SlateConfigModel


class TestSlateConfigLoadFromDict(unittest.TestCase):
    def test_load_from_dict(self):
        slate_dict = {
            "id": "c410516f-18b3-46a1-b356-c7c003de2b53",
            "displayName": "Trending Articles",
            "description": "Curated articles"
        }

        slate_config = SlateConfigModel.load_from_dict(slate_dict)
        self.assertEqual(slate_config.id, "c410516f-18b3-46a1-b356-c7c003de2b53")
        self.assertEqual(slate_config.description, "Curated articles")
        self.assertEqual(slate_config.displayName, "Trending Articles")
