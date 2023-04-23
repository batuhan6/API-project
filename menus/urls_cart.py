from django.urls import path
from rest_framework.routers import DefaultRouter
from menus import views_cart

router = DefaultRouter()
router.register('menu-items', views_cart.CartListOrCreateAPIViewSet, basename='cart')

urlpatterns = [
    path("menu-items/<int:pk>", views_cart.CartRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns += router.urls