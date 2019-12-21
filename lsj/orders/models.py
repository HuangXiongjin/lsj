from django.db import models

from goods.models import Goods
from users.models import User


class Order(models.Model):
    """用户订单表"""
    # 订单编号
    no = models.CharField(max_length=512, null=False)
    # 用户id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 订单详情
    detail = models.CharField(max_length=1024, null=True)
    # 支付状态(0：未付款，1:已付款，未发货，2：待收货)
    pay_status = models.IntegerField(default=0)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'


class OrderGoods(models.Model):
    """订单与商品表"""
    # 关联的商品
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    # 关联的订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # 商品个数
    goods_num = models.IntegerField(default=1)

    class Meta:
        db_table = 'goods_order'
