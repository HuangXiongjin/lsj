import re

from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from users.models import User
from utils.handler_errors import ParamsException
from utils.status_code import ERROR_USER_EXISTS, ERROR_PASSWORD_DIFFERENT, ERROR_MOBILE, ERROR_USER_PASSWORD


class UserSerializers(serializers.ModelSerializer):
    """用户序列化"""
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.Serializer):
    """用户注册序列化类"""
    u_username = serializers.CharField(required=True, max_length=15, min_length=8,
                                       error_messages={'required': '用户名不能为空',
                                                       'max_length': '最大长度15',
                                                       'min_length': '最小长度8'})

    u_password = serializers.CharField(required=True, max_length=10, min_length=6,
                                       error_messages={'required': '密码不能为空',
                                                       'max_length': '最大长度10',
                                                       'min_length': '最小长度6'})

    u_password2 = serializers.CharField(required=True, max_length=10, min_length=6,
                                        error_messages={'required': '确认密码不能为空',
                                                        'max_length': '最大长度15',
                                                        'min_length': '最小长度6'})

    u_mobile = serializers.CharField(required=True, error_messages={'required': '该参数必填'})

    def validate(self, attrs):
        """
        1.验证账号是否存在
        2.密码是否一致
        3.邮箱格式是否正确
        """
        if User.objects.filter(username=attrs.get('u_username')).first():
            raise ParamsException({'code': ERROR_USER_EXISTS[0], 'msg': ERROR_USER_EXISTS[1]})
        if attrs.get('u_password') != attrs.get('u_password2'):
            raise ParamsException({'code': ERROR_PASSWORD_DIFFERENT[0], 'msg': ERROR_PASSWORD_DIFFERENT[1]})
        MOBILE_PATTERN = re.compile(r'1[3-9]\d{9}')
        if not MOBILE_PATTERN.fullmatch(attrs.get('u_mobile')):
            raise ParamsException({'code': ERROR_MOBILE[0], 'msg': ERROR_MOBILE[1]})
        return attrs


class UserLoginSerializer(serializers.Serializer):
    """用户登录"""
    u_username = serializers.CharField(required=True, max_length=15, min_length=8,
                                       error_messages={'required': '用户名不能为空',
                                                       'max_length': '最大长度15',
                                                       'min_length': '最小长度8'})

    u_password = serializers.CharField(required=True, max_length=10, min_length=6,
                                       error_messages={'required': '密码不能为空',
                                                       'max_length': '最大长度10',
                                                       'min_length': '最小长度6'})

    def validate(self, attrs):
        user = User.objects.filter(username=attrs.get('u_username')).first()
        if user and check_password(attrs.get('u_password'), user.password):
            return attrs
        raise ParamsException({'code': ERROR_USER_PASSWORD[0], 'msg': ERROR_USER_PASSWORD[1]})
