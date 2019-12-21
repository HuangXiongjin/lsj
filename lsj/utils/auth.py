from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from users.models import User
from utils.handler_errors import ParamsException
from utils.status_code import ERROR_USER_INVALID


class UserAuth(BaseAuthentication):
    def authenticate(self, request):
        allow_path = ['/api/user/auth/register/',
                      '/api/user/auth/login/',
                      '/api/goods/home/',
                      '/api/goods/foodtype/',
                      '/api/goods/market/']
        if request.path not in allow_path:
            token = request.data.get('token') if request.data.get('token') else request.query_params.get('token')
            if token:
                user = User.objects.get(pk=cache.get(token))
                return user, token
            raise ParamsException({'code': ERROR_USER_INVALID[0], 'msg': ERROR_USER_INVALID[1]})
        return None
