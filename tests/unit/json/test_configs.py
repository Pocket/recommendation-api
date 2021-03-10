from collections import Counter
from app.json.utils import parse_to_dict


class TestConfigs():

    def setup(self):
        self.lineups = parse_to_dict("./app/json/slate_lineup_configs.json",
                                     "./app/json/slate_lineup_config.schema.json")

        self.slates = parse_to_dict("./app/json/slate_configs.json",
                                    "./app/json/slate_config.schema.json")

        self.guid_attr = "id"

    def test_lineup_guids_unique(self):
        guids = [r[self.guid_attr] for r in self.lineups]
        c = Counter(guids)
        for guid, count in c.items():
            assert count == 1

    def test_slate_guids_unique(self):
        guids = [r[self.guid_attr] for r in self.slates]
        c = Counter(guids)
        for guid, count in c.items():
            assert count == 1

    def test_fields_exist(self):

        slate_guids = {r['id']: r for r in self.slates}
        for lineup in self.lineups:
            assert "id" in lineup
            assert "description" in lineup
            for experiment in lineup['experiments']:
                assert "description" in experiment
                for slate_id in experiment['slates']:
                    assert slate_id in slate_guids
                    assert "displayName" in slate_guids[slate_id]
                    for slate_experiment in slate_guids[slate_id]["experiments"]:
                        assert "description" in slate_experiment
