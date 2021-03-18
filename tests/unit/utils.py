import random
from typing import List
from app.models.recommendation import RecommendationModel
from app.models.item import ItemModel


def generate_recommendations(item_ids: List[int or str]) -> List[RecommendationModel]:
    recs = []
    for item_id in item_ids:
        rec = RecommendationModel(
            item_id=item_id,
            item=ItemModel(item_id=item_id),
            rec_src='bowling',
            feed_id=random.randint(0, 101),
            feed_item_id=random.randint(0, 101),
            id=random.randint(0, 101)
        )
        recs.append(rec)

    return recs
