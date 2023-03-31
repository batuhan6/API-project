from rest_framework import generics
from orders.models import Order, OrderItem
from orders import serializers


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderUpdateSerializer


class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDeleteSerializer
