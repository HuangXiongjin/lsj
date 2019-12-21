from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from carts.models import Cart
from carts.serializers import CartSerializer
from utils.auth import UserAuth
from utils.func import manage_cart
from utils.status_code import SUCCESS


class CartView(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # 局部认证
    # authentication_classes = (UserAuth, )

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.get_queryset().filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        total_price = 0
        all_select = 1
        for item in queryset:
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
        instance = self.get_object()
        instance.is_select = not instance.is_select
        instance.save()
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1]})

    @action(methods=['POST'], detail=False)
    def add_cart(self, request):
        manage_cart(request, 1)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[2]})

    @action(methods=['POST'], detail=False)
    def sub_cart(self, request):
        manage_cart(request, 0)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[3]})

    @action(methods=['PATCH'], detail=False)
    def change_select(self, request):
        user = request.user
        if Cart.objects.filter(user=user, is_select=False).exists():
            Cart.objects.filter(user=user).update(is_select=True)
        else:
            Cart.objects.filter(user=user).update(is_select=False)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1]})
