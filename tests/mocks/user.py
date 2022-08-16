import pytest

from app.models.user_ids import UserIds


@pytest.fixture
def user_1():
    return UserIds(
        user_id=1,
        hashed_user_id='1-hashed',
        guid=9876,
        hashed_guid='9876-hashed'
    )
