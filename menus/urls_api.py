from django.urls import path
from rest_framework.routers import DefaultRouter

from menus import views_api

router = DefaultRouter()
router.register('', views_api.MenuItemListOrCreateAPIViewSet, basename='menu-items')

urlpatterns = [
    path("<int:pk>", views_api.MenuItemDetailUpdateDestroyAPIView.as_view()),
]

urlpatterns += router.urls
