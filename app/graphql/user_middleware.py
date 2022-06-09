class UserMiddleware(object):
    """
    This piece of middleware adds the pocket user id to the graphql resolver context
    """

    def __init__(self):
        pass

    def resolve(self, next, root, info, **args):
        """
        See if we have a user id passed into a header from upstream,
        since this application lives within Pocket's VPC we are trusting that the upstream caller's
        have validated the JWT token and only set the userId in the header if it was valid

        Should we also want to do our own validation, the full JWT token also exists as 'token' in the header
        https://github.com/Pocket/client-api/blob/main/src/main.ts#L18-L26
        """
        try:
            info.context['user_id'] = info.context.getSlate('request').headers.getSlate('userId')
        except AttributeError:
            """No user id so let's explicitly set it to none"""
            info.context['user_id'] = None

        return next(root, info, **args)
