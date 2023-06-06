from rest_framework import serializers
from orders.models import Order
from orders.serializers import OrderItemListSerializer


class OrderListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_items(self, obj):
        order_items = obj.order_items.all()
        serializer = OrderItemListSerializer(order_items, many=True)
        return serializer.data


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
