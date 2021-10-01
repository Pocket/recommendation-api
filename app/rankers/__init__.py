def get_ranker(name):
    return get_all_rankers()[name]

PERSONALIZED_RANKERS = {"top1-topics", "top3-topics", "rank-topics"}

THOMPSON_SAMPLING_RANKERS = {"thompson-sampling-1day", "thompson-sampling-7day",
                             "thompson-sampling-14day", "thompson-sampling-28day"}

def get_all_rankers():
    # Importing algorithms within the function here ensures that when rankers are imported
    # they do not cause unwanted circular imports.
    #
    # For example, if the RecommendationModel uses rankers:
    #
    # `RecommendationModel` imports `app.rankers` which imports `algorithms` which in itself imports
    # `RecommendationModel`. - This will result in the following error:
    # ImportError: cannot import name 'RecommendationModel' from partially initialized module
    # 'app.models.recommendation' (most likely due to a circular import) (/opt/project/app/models/recommendation.py)
    #
    # For the above, importing algorithms within this function means that the `algorithms` import only happens
    # when rankers are needed which means the `RecommendationModel` will fully be initialized before
    # `algorithms` attempt to import `RecommendationModel` - Getting us out of the circular import problem.
    from app.rankers.algorithms import (
        top5,
        top15,
        top30,
        top45,
        thompson_sampling,  # this uses a 28 day window by default
        thompson_sampling_1day,
        thompson_sampling_7day,
        thompson_sampling_14day,
        spread_publishers,
        top1_topics,
        top3_topics,
        rank_topics
    )

    return {
        'top5': top5,
        'top15': top15,
        'top30': top30,
        'top45': top45,
        'thompson-sampling-1day': thompson_sampling_1day,
        'thompson-sampling-7day': thompson_sampling_7day,
        'thompson-sampling-14day': thompson_sampling_14day,
        'thompson-sampling-28day': thompson_sampling,
        'top1-topics': top1_topics,
        'top3-topics': top3_topics,
        'rank-topics': rank_topics,
        'pubspread': spread_publishers
    }
