from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views_api import DeliveryCrewListOrCreateAPIViewSet, DeliveryCrewDeleteAPIView

router = DefaultRouter()
router.register(r'users', DeliveryCrewListOrCreateAPIViewSet, basename='users')

urlpatterns = [
    path("users/<int:pk>", DeliveryCrewDeleteAPIView.as_view()),
]

urlpatterns += router.urls
