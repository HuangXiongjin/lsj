from rest_framework import serializers

from goods.serializers import GoodsSerializer
from orders.models import OrderGoods, Order


class OrderSerializer(serializers.ModelSerializer):
    """订单序列化"""
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        """自定义返回的数据格式，继承父类的to_representation方法"""
        data = super(OrderSerializer, self).to_representation(instance)
        order_goods = instance.ordergoods_set.all()
        data['order_goods_info'] = OrderGoodsSerializer(order_goods, many=True).data
        total_price = 0
        for items in order_goods:
            total_price += items.goods.price * items.goods_num
            data['o_price'] = total_price
        return data


class OrderGoodsSerializer(serializers.ModelSerializer):
    """订单商品序列化"""
    goods = GoodsSerializer()

    class Meta:
        model = OrderGoods
        fields = '__all__'

    def to_representation(self, instance):
        data = super(OrderGoodsSerializer, self).to_representation(instance)
        data['o_goods'] = data['goods']
        return data
