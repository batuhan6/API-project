from django.urls import path
from rest_framework.routers import DefaultRouter
from orders import views_api

#router = DefaultRouter()
#router.register('', views_api.OrderListOrCreateAPIViewSet, basename='orders')

urlpatterns = [
    # path("<int:pk>", views_api.OrderDetailAPIView.as_view()),
    # path("<int:pk>", views_api.OrderUpdateAPIView.as_view()),
    # path("<int:pk>", views_api.OrderDeleteAPIView.as_view()),

    #path("<int:pk>", views_api.OrderDetailUpdateDestroyAPIView.as_view()),
]

# urlpatterns += router.urls