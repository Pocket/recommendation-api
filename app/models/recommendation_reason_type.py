from enum import Enum


class RecommendationReasonType(str, Enum):
    POCKET_HITS = 'POCKET_HITS'
    PREFERRED_TOPICS = 'PREFERRED_TOPICS'
    SIMILAR_TO_ENGAGED = 'SIMILAR_TO_ENGAGED'
