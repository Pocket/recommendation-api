import random
from typing import List
from app.models.recommendation import RecommendationModel
from app.models.item import ItemModel
from app.models.slate_lineup_config import SlateLineupConfigModel
from app.models.slate_config import SlateConfigModel

ALL_CURATED_TOPICS_LINEUP = "55f5ed88-c7d9-48f9-bcf1-7ad214684ee9"

def generate_recommendations(item_ids: List[int or str]) -> List[RecommendationModel]:
    recs = []
    for item_id in item_ids:
        rec = RecommendationModel(
            item_id=item_id,
            item=ItemModel(item_id=str(item_id)),
            rec_src='bowling',
            feed_id=random.randint(0, 101),
            id=random.randint(0, 101)
        )
        rec.feed_item_id = rec.id
        recs.append(rec)

    return recs

def generate_curated_configs() -> List[SlateConfigModel]:
    '''
    This returns slateIDs for curated not new tab slates for all 15 original topic labels
    :return:
    '''

    initialize_slate_lineups()

    input_lineup = SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID[ALL_CURATED_TOPICS_LINEUP]
    input_slates = input_lineup.experiments[0].slates
    input_configs = []
    for slate_id in input_slates:
        input_configs.append(SlateConfigModel.find_by_id(slate_id))

    return input_configs


def initialize_slate_lineups():
    slate_configs = SlateConfigModel.load_slate_configs()
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in slate_configs}
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()
    SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID = {lc.id: lc for lc in slate_lineup_configs}


def generate_nontopic_configs() -> List[SlateConfigModel]:
    slate_configs = SlateConfigModel.load_slate_configs()
    # Two non-topic slates
    input_slates = ["de254c5d-57a7-4553-850f-153ee385014d", "48e766be-5e96-46fb-acbf-55fee3ae8a28"]
    input_configs = [c for c in slate_configs if c.id in input_slates]

    return input_configs

def generate_lineup_configs(lineup_id: str):
    # get slate configs from lineup_id
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()
    slate_configs = SlateConfigModel.load_slate_configs()
    x = [x for x in slate_lineup_configs if x.id == lineup_id]
    slate_ids = x[0].experiments[0].slates
    return [c for c in slate_configs if c.id in slate_ids], x[0].description

