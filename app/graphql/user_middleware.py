from app.models.user_session_ids import UserSessionIds


class UserMiddleware(object):
    """
    This piece of middleware adds the pocket user id to the graphql resolver context
    """

    def __init__(self):
        pass

    def resolve(self, next, root, info, **args):
        """
        See if we have a user/guid id (hashed or unhashed) passed into a header from upstream,
        since this application lives within Pocket's VPC we are trusting that the upstream caller's
        have validated the JWT token and only set the userId in the header if it was valid

        Should we also want to do our own validation, the full JWT token also exists as 'token' in the header
        https://github.com/Pocket/client-api/blob/main/src/main.ts#L18-L26
        """
        headers = info.context.get('request').headers

        info.context['user_id'] = headers.get('userId')

        info.context['user_session_ids'] = UserSessionIds(
            user_id=headers.get('userId'),
            hashed_user_id=headers.get('Encodedid'),
            hashed_guid=headers.get('Encodedguid'),
            guid=headers.get('Guid'),
        )

        return next(root, info, **args)
