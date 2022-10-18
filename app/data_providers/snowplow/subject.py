from aio_snowplow_tracker import Subject

from app.models.user_ids import UserIds


def get_subject(user_ids: UserIds) -> Subject:
    """
    :param user_ids:
    :return: Snowplow Subject
    """
    return Subject().set_user_id(str(user_ids.user_id))
