import random
import os
from typing import List
from app.models.recommendation import RecommendationModel
from app.models.item import ItemModel
from app.models.slate_lineup_config import SlateLineupConfigModel
from app.models.slate_config import SlateConfigModel

WEB_HOME_LINEUP_ID = "55f5ed88-c7d9-48f9-bcf1-7ad214684ee9"


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

    input_lineup = SlateLineupConfigModel.SLATE_LINEUP_CONFIGS_BY_ID[WEB_HOME_LINEUP_ID]
    input_slates = input_lineup.experiments[0].slates
    input_configs = []
    for slate_id in input_slates:
        input_configs.append(SlateConfigModel.find_by_id(slate_id))

    return input_configs
