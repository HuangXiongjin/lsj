import django_filters


from orders.models import Order


class OrderFilter(django_filters.rest_framework.FilterSet):
    """定义订单过滤类"""
    o_status = django_filters.CharFilter(method='filter_pay_status')

    class Meta:
        model = Order
        fields = '__all__'

    def filter_pay_status(self, queryset, name, value):
        """判断当前的订单状态，返回指定的商品"""
        if value == 'not_pay':
            return queryset.filter(pay_status=0)
        elif value == 'not_send':
            return queryset.filter(pay_status=1)
        else:
            return queryset.filter(pay_status=2)
