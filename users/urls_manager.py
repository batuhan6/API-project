from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views_api import ManagerListOrCreateAPIViewSet, ManagerDeleteAPIView

router = DefaultRouter()
router.register(r'users', ManagerListOrCreateAPIViewSet, basename='users')

urlpatterns = [
    path("users/<int:pk>", ManagerDeleteAPIView.as_view()),
]

urlpatterns += router.urls
