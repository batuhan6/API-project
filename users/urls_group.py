from django.urls import path
from rest_framework.routers import DefaultRouter
#from users import views_api
from users.views_api import UserListOrCreateAPIViewSet, UserDeleteAPIView

router = DefaultRouter()
router.register(r'users', UserListOrCreateAPIViewSet, basename='users')

urlpatterns = [
    path("users/<int:pk>", UserDeleteAPIView.as_view()),
]

urlpatterns += router.urls
