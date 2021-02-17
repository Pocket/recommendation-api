import random
from typing import List
from app.models.recommendation import RecommendationModel
from app.models.item import ItemModel


def generate_recommendations(item_ids: List[int or str]) -> List[RecommendationModel]:
    recs = []
    for item_id in item_ids:
        rec = RecommendationModel()
        rec.item_id = item_id
        rec.item = ItemModel(item_id=item_id)
        rec.feed_id = random.randint(0, 101)
        rec.feed_item_id = random.randint(0, 101)
        rec.rec_src = 'bowling'
        recs.append(rec)

    return recs
