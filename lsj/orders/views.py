import uuid

from rest_framework import viewsets, mixins
from rest_framework.response import Response

from carts.models import Cart
from orders.filters import OrderFilter
from orders.models import Order, OrderGoods
from orders.serializers import OrderSerializer
from utils.status_code import ERROR_ORDER, SUCCESS_ORDER


class OrderView(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    """订单详情"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # 定义过滤类
    filter_class = OrderFilter

    def list(self, request, *args, **kwargs):
        """查看订单"""
        # 获取当前登录用户
        result = self.get_queryset().filter(user=request.user)
        # 获取当前用户的订单信息
        queryset = self.filter_queryset(result)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """创建订单"""
        user = request.user
        # 将当前用户的购物车中已选择的商品添加到订单中
        carts = Cart.objects.filter(user=user, is_select=True).all()
        if carts.count() != 0:
            # 生成唯一的订单编号，绑定用户信息
            order_no = uuid.uuid4().hex
            order = Order.objects.create(no=order_no, user=user)
            for cart in carts:
                # 创建订单商品中间表
                OrderGoods.objects.create(order=order, goods=cart.goods, goods_num=cart.num)
                # 将购物车中已经下单的商品删除
                cart.delete()
            return Response({'code': SUCCESS_ORDER[0], 'msg': SUCCESS_ORDER[1]})
        return Response({'code': ERROR_ORDER[0], 'msg': ERROR_ORDER[1]})
