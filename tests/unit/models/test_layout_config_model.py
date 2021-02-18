import unittest

from app.models.layout_config import LayoutConfigModel


class TestLayoutConfigLoadFromDict(unittest.TestCase):
    def test_load_from_dict(self):
        layout_dict = {
            "id": "c410516f-18b3-46a1-b356-c7c003de2b53",
            "description": "Topical layout"
        }

        layout_config = LayoutConfigModel.load_from_dict(layout_dict)
        self.assertEqual(layout_config.id, "c410516f-18b3-46a1-b356-c7c003de2b53")
        self.assertEqual(layout_config.description, "Topical layout")
