from rest_framework.routers import SimpleRouter

from users.views import UserView

route = SimpleRouter()
route.register('auth', UserView)

urlpatterns = [

]

urlpatterns += route.urls




