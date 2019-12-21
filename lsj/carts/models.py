from django.db import models

from goods.models import Goods
from users.models import User


class Cart(models.Model):
    """购物车"""
    # 商品id
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # 用户id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 商品个数
    num = models.IntegerField(default=1)
    # 是否选择该商品
    is_select = models.BooleanField(default=1)

    class Meta:
        db_table = 'cart'
