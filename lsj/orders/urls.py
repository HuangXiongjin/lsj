from rest_framework.routers import SimpleRouter

from orders.views import OrderView

route = SimpleRouter()
route.register('orders', OrderView)

urlpatterns = [

]

urlpatterns += route.urls
