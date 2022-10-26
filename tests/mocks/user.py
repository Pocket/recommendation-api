import pytest

from app.models.request_user import RequestUser


@pytest.fixture
def user_1():
    return RequestUser(
        user_id=1,
        hashed_user_id='1-hashed',
        guid=9876,
        hashed_guid='9876-hashed'
    )
