from django.db import models


class User(models.Model):
    """用户表"""
    # 用户名
    username = models.CharField(max_length=32, unique=True, null=False)
    # 用户密码
    password = models.CharField(max_length=256, null=False)
    # 电话
    mobile = models.CharField(max_length=11, null=False)
    # 用户头像
    icon = models.ImageField(null=True)
    # 用户状态（1：正常，0：禁用）
    status = models.BooleanField(default=1)

    class Meta:
        db_table = 'user'
