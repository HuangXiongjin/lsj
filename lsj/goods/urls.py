from django.urls import path
from rest_framework.routers import SimpleRouter

from goods.views import home, FoodTypeView, MarketView

route = SimpleRouter()

route.register('market', MarketView)
route.register('foodtype', FoodTypeView)

urlpatterns = [
    path('home/', home),
]

urlpatterns += route.urls
