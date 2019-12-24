import django_filters

from goods.models import Goods, FoodType


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """定义当前分类中的商品"""
    # 通过method自定义过滤的方法
    typeid = django_filters.CharFilter(method='filter_category')
    childcid = django_filters.CharFilter(method='filter_childid')
    order_rule = django_filters.CharFilter(method='filter_order_rule')

    class Meta:
        model = Goods
        fields = []

    def filter_category(self, queryset, name, value):
        """将左边栏分类与商品详细分类关联在一起"""
        food_type = FoodType.objects.filter(type_no=value).first()
        return queryset.filter(category_id=food_type.id)

    def filter_childid(self, queryset, name, value):
        """根据商品详细分类的值，获取对应的商品"""
        if value == '0':
            return queryset
        else:
            return queryset.filter(childid=value)

    def filter_order_rule(self, queryset, name, value):
        """根据商品的排序值，对商品进行排序"""
        if value == '0':
            return queryset.order_by('price')
        if value == '1':
            return queryset.order_by('-price')
        if value == '2':
            return queryset.order_by('sale_num')
        if value == '3':
            return queryset.order_by('-sale_num')
