from rest_framework.routers import SimpleRouter

from carts.views import CartView

route = SimpleRouter()

route.register('cart', CartView)

urlpatterns = [

]

urlpatterns += route.urls




