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
            item=ItemModel(item_id=item_id),
            rec_src='bowling',
            feed_id=random.randint(0, 101),
            id=random.randint(0, 101)
        )
        rec.feed_item_id = id
        recs.append(rec)

    return recs

def generate_curated_configs() -> List[SlateConfigModel]:
    '''
    This returns slateIDs for curated not new tab slates for all 15 original topic labels
    :return:
    '''

    slate_configs = SlateConfigModel.load_slate_configs()
    SlateConfigModel.SLATE_CONFIGS_BY_ID = {s.id: s for s in slate_configs}
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()
    SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID = {lc.id: lc for lc in slate_lineup_configs}

    input_lineup = SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID[ALL_CURATED_TOPICS_LINEUP]
    input_slates = input_lineup.experiments[0].slates
    input_configs = []
    for slate_id in input_slates:
        input_configs.append(SlateConfigModel.find_by_id(slate_id))

    return input_configs

def generate_uncurated_configs() -> List[SlateConfigModel]:

    slate_configs = SlateConfigModel.load_slate_configs()
    # two algorithmic topic slates
    input_slates = ["d024ce9c-ed96-453f-a81e-8a0b850681e7", "fa61096a-b681-4251-b299-2fda06c49ebf"]
    input_configs = [c for c in slate_configs if c.id in input_slates]

    return input_configs

def generate_lineup_configs(lineup_id: str):
    # get slate configs from lineup_id
    slate_lineup_configs = SlateLineupConfigModel.load_slate_lineup_configs()
    slate_configs = SlateConfigModel.load_slate_configs()
    x = [x for x in slate_lineup_configs if x.id == lineup_id]
    slate_ids = x[0].experiments[0].slates
    return [c for c in slate_configs if c.id in slate_ids], x[0].description

