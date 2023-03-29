from django.urls import path, include
from users import views_api

urlpatterns = [
    path('users', views_api.UserCreateAPIView.as_view()),
    path('users/', include('users.urls_user')),

]
