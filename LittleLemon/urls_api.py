from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from orders.views_api import OrderListAPIView

urlpatterns = [
    path('', include('users.urls_api'), name="users"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #    path('orders', OrderListAPIView.as_view()),
    path('orders/', include('orders.urls_api'), name="orders"),
    path('menu-items/', include('menus.urls_api'), name="menu-items"),
    path('groups/', include('users.urls_api'), name="users"),
    path('cart/', include('menus.urls_cart'), name="cart"),
]
