import unittest

from app.graphql.user_middleware import UserMiddleware


class Request(object):
    headers: dict = {}

    def __init__(self, headers: dict):
        self.headers = headers


class ResolveInfo(object):
    context = {}

    def __init__(self, request: Request):
        self.context = {
            'request': request
        }


class TestUserMiddleware(unittest.TestCase):

    def test_user_middleware_adds_user_id(self):
        middleware = UserMiddleware()

        info = ResolveInfo(
            request=Request(headers={
                'userId': '12345'
            }))

        response = middleware.resolve(next=TestUserMiddleware.nextStub, root={}, info=info)
        assert '12345' == response.context['user_id']

    def test_user_middleware_no_user_id(self):
        middleware = UserMiddleware()

        info = ResolveInfo(
            request=Request(headers={
            }))

        response = middleware.resolve(next=TestUserMiddleware.nextStub, root={}, info=info)
        assert response.context['user_id'] is None

    @staticmethod
    def nextStub(root, info, **kwargs):
        return info
