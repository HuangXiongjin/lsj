from rest_framework import serializers

from carts.models import Cart
from goods.serializers import GoodsSerializer


class CartSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

    def to_representation(self, instance):
        data = super(CartSerializer, self).to_representation(instance)
        data['c_is_select'] = data['is_select']
        data['c_goods_num'] = data['num']
        data['c_goods'] = data['goods']
        return data
