from rest_framework import serializers

from carts.models import Cart
from goods.serializers import GoodsSerializer


class CartSerializer(serializers.ModelSerializer):
    """购物车序列化"""
    goods = GoodsSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        """重写父类的to_representation方法，返回自己需要的数据格式"""
        data = super(CartSerializer, self).to_representation(instance)
        data['c_is_select'] = data['is_select']
        data['c_goods_num'] = data['num']
        data['c_goods'] = data['goods']
        return data
