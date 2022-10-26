from aio_snowplow_tracker import Subject

from app.models.request_user import RequestUser


def get_subject(user: RequestUser) -> Subject:
    """
    :param user:
    :return: Snowplow Subject
    """
    return Subject().set_user_id(str(user.user_id))
