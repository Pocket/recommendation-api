def get_ranker(name):
    return get_all_rankers()[name]


def get_all_rankers():
    from app.rankers.algorithms import (
        top15,
        top30,
        thompson_sampling,
        spread_publishers
    )

    return {
        'top15': top15,
        'top30': top30,
        'thompson-sampling': thompson_sampling,
        'pubspread': spread_publishers
    }