from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_spectacular import views as spectacular_views

urlpatterns = [
    path('', include('users.urls_api'), name="users"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/', include('orders.urls_api'), name="orders"),
    path('menu-items/', include('menus.urls_api'), name="menu-items"),
    path('groups/', include('users.urls_api'), name="groups"),
    path('cart/', include('menus.urls_cart'), name="cart"),

    path('docs/default/',
         spectacular_views.SpectacularAPIView.as_view(),
         name='schema'),
    path('docs/redoc/', spectacular_views.SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),
    path('docs/', spectacular_views.SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
]
