from app.rankers.algorithms import (
    top15,
    top30,
    thompson_sampling,
    spread_publishers
)


RANKERS = {
    'top15': top15,
    'top30': top30,
    'thompson-sampling': thompson_sampling,
    'pubspread': spread_publishers
}
