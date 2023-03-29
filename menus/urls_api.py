from django.urls import path
from menus import views_api

urlpatterns = [
    path("<int:pk>", views_api.MenuItemDetailAPIView.as_view()),
    path("<int:pk>", views_api.MenuItemUpdateAPIView.as_view()),
    path("<int:pk>", views_api.MenuItemDeleteAPIView.as_view()),
]
