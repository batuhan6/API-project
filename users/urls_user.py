from django.urls import path
from users import views_api


urlpatterns = [
    path('me', views_api.UserDetailAPIView.as_view()),
    path("login", views_api.UserLoginAPIView.as_view()),
]
