from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from goods.filters import GoodsFilter
from goods.models import MainNav, MainWheel, MainShow, FoodType, Goods
from goods.serializers import MainNavSerializer, MainWheelSerializer, MainShowSerializer, FoodTypeSerializer, \
    GoodsSerializer
from utils.status_code import SUCCESS


@api_view(['GET'])
def home(request):
    mainnav = MainNav.objects.all()
    mainwheel = MainWheel.objects.all()
    mainshow = MainShow.objects.all()
    data = {
        'main_navs': MainNavSerializer(mainnav, many=True).data,
        'main_wheels': MainWheelSerializer(mainwheel, many=True).data,
        'main_shows': MainShowSerializer(mainshow, many=True).data
    }
    return Response({'code': SUCCESS[0], 'data': data})


class FoodTypeView(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
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
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
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
        food_type = FoodType.objects.filter(type_no=type_no).first()
        type_name = food_type.child_type_name
        results = [item.split(':') for item in type_name.split('#')]
        foodtype_childname_list = []
        for item in results:
            dict1 = {'child_name': item[0], 'child_value': item[1]}
            foodtype_childname_list.append(dict1)
        data = {
            'goods_list': serializer.data,
            'foodtype_childname_list': foodtype_childname_list,
            'order_rule_list': rule_list,
        }
        return Response({'code': SUCCESS[0], 'msg': SUCCESS[1], 'data': data})
