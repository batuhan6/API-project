from rest_framework.routers import DefaultRouter
from orders import views_api

router = DefaultRouter()
router.register('', views_api.OrderListOrCreateAPIViewSet, basename='orders')

urlpatterns = [

]

urlpatterns += router.urls
