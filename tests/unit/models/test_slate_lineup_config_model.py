import unittest

from app.models.slate_lineup_config import SlateLineupConfigModel


class TestSlateLineupConfigLoadFromDict(unittest.TestCase):
    def test_load_from_dict(self):
        slate_lineup_dict = {
            "id": "c410516f-18b3-46a1-b356-c7c003de2b53",
            "description": "Topical slate_lineup"
        }

        slate_lineup_config = SlateLineupConfigModel.load_from_dict(slate_lineup_dict)
        self.assertEqual(slate_lineup_config.id, "c410516f-18b3-46a1-b356-c7c003de2b53")
        self.assertEqual(slate_lineup_config.description, "Topical slate_lineup")
