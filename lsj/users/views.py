import uuid

from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializers, UserRegisterSerializer, UserLoginSerializer
from utils.status_code import ERROR_FIELD


class UserView(viewsets.GenericViewSet,
               mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def list(self, request, *args, **kwargs):
        user = request.user
        data = {'username': user.username,
                'order_not_pay_num': '',
                'order_not_send_num': ''}
        return Response(data)

    @action(methods=['POST'], detail=False, serializer_class=UserRegisterSerializer)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if result:
            password = make_password(serializer.data['u_password'])
            user = User.objects.create(username=serializer.data['u_username'],
                                       password=password,
                                       mobile=serializer.data['u_mobile'])
            return Response({'user_id': user.id})
        error_message = {key: values[0] for key, values in serializer.errors.items()}
        return Response({'code': ERROR_FIELD[0], 'msg': error_message})

    @action(methods=['POST'], detail=False, serializer_class=UserLoginSerializer)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=False)
        if result:
            token = uuid.uuid4().hex
            user = User.objects.filter(username=serializer.data['u_username']).first()
            cache.set(token, user.id, timeout=30000)
            return Response({'token': token})
        error_message = {key: values[0] for key, values in serializer.errors.items()}
        return Response({'code': ERROR_FIELD[0], 'msg': error_message})
