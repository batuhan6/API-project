from django.urls import path, include

from menus.views_api import MenuItemListAPIView

urlpatterns = [
    path('orders/', include('orders.urls_api'), name="orders"),
    path('menu-items', MenuItemListAPIView.as_view()),
    path('menu-items/', include('menus.urls_api'), name="menu-items"),
    path('users/', include('users.urls_api'), name="users"),
    #path('groups/', include(''))
]
