from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from carts.models import Cart
from carts.serializers import CartSerializer
from utils.func import manage_cart
from utils.status_code import SUCCESS


class CartView(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin):
    """购物车"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        """显示购物车商品"""
        user = request.user
        # 获取当前用户的的购物车信息
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        total_price = 0
        all_select = 1
        for item in queryset:
            # 计算选择商品的总价
            if item.is_select:
                total_price += item.num * item.goods.price
            else:
                all_select = 0
        data = {'carts': serializer.data,
                'total_price': total_price,
                'all_select': all_select,
                'username': user.username,
                'mobile': user.mobile}
        return Response(data)

    def update(self, request, *args, **kwargs):
        """修改商品选择"""
        # 获取到当前的对象实例
        instance = self.get_object()
        instance.is_select = not instance.is_select
        instance.save()
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1]})

    @action(methods=['POST'], detail=False)
    def add_cart(self, request):
        """添加商品到购物车"""
        manage_cart(request, 1)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[2]})

    @action(methods=['POST'], detail=False)
    def sub_cart(self, request):
        """删除商品"""
        manage_cart(request, 0)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[3]})

    @action(methods=['PATCH'], detail=False)
    def change_select(self, request):
        """是否全选商品"""
        user = request.user
        if Cart.objects.filter(user=user, is_select=False).exists():
            # 判断是否有未选择的商品，如果有将选择属性修改为True
            Cart.objects.filter(user=user).update(is_select=True)
        else:
            Cart.objects.filter(user=user).update(is_select=False)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1]})
