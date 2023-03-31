from django.urls import path

from orders import views_api

urlpatterns = [
    path("<int:pk>", views_api.OrderDetailAPIView.as_view()),
    path("<int:pk>", views_api.OrderUpdateAPIView.as_view()),
    path("<int:pk>", views_api.OrderDeleteAPIView.as_view()),
]
