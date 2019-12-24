from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from goods.filters import GoodsFilter
from goods.models import MainNav, MainWheel, MainShow, FoodType, Goods
from goods.serializers import MainNavSerializer, MainWheelSerializer, MainShowSerializer, FoodTypeSerializer, \
    GoodsSerializer
from utils.func import manage_cart
from utils.status_code import SUCCESS


@api_view(['GET'])
def home(request):
    """主页商品"""
    mainnav = MainNav.objects.all()
    mainwheel = MainWheel.objects.all()
    mainshow = MainShow.objects.all()
    data = {
        'main_navs': MainNavSerializer(mainnav, many=True).data,
        'main_wheels': MainWheelSerializer(mainwheel, many=True).data,
        'main_shows': MainShowSerializer(mainshow, many=True).data
    }
    return Response({'code': SUCCESS[0], 'data': data})


@api_view(['POST'])
def cart(request):
    """购物车"""
    manage_cart(request, 1)
    return Response({'code': SUCCESS[0], 'msg': SUCCESS[2]})


class FoodTypeView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    """左边栏商品分类"""
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        results = serializer.data
        data = []
        for item in results:
            dict1 = {'id': item['id'], 'typeid': item['type_no'], 'typename': item['type_name']}
            data.append(dict1)
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1], 'data': data})


class MarketView(viewsets.GenericViewSet,
                 mixins.ListModelMixin):
    """商品分类信息"""
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # 定义商品分类过滤
    filter_class = GoodsFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        rule_list = [
            {'order_name': '价格升序', 'order_value': '0'},
            {'order_name': '价格降序', 'order_value': '1'},
            {'order_name': '销量升序', 'order_value': '2'},
            {'order_name': '销量降序', 'order_value': '3'},
        ]
        type_no = request.query_params.get('typeid')
        # 获取当前商品的分类信息
        food_type = FoodType.objects.filter(type_no=type_no).first()
        type_name = food_type.child_type_name
        # 整理分类信息，全部分类:0#进口水果:103534#国产水果:103533
        # 修改为['全部分类': 0, '进口水果': 103545, '国产水果': 103533]
        results = [item.split(':') for item in type_name.split('#')]
        foodtype_childname_list = []
        for item in results:
            dict1 = {'child_name': item[0], 'child_value': item[1]}
            foodtype_childname_list.append(dict1)
        # 定义前端接收的数据格式
        data = {
            'goods_list': serializer.data,
            'foodtype_childname_list': foodtype_childname_list,
            'order_rule_list': rule_list,
        }
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1], 'data': data})
