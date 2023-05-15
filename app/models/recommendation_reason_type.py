from enum import Enum


class RecommendationReasonType(str, Enum):
    POCKET_HITS = 'POCKET_HITS'
    PREFERRED_TOPICS = 'PREFERRED_TOPICS'
    HYBRID_CF_RECOMMENDER = 'HYBRID_CF_RECOMMENDER'
