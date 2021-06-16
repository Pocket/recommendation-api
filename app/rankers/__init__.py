def get_ranker(name):
    return get_all_rankers()[name]


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
        thompson_sampling,
        spread_publishers,
        personalize_topic_slates
    )

    return {
        'top5': top5,
        'top15': top15,
        'top30': top30,
        'top45': top45,
        'thompson-sampling': thompson_sampling,
        'personalized-topics': personalize_topic_slates,
        'pubspread': spread_publishers
    }
