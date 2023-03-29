from rest_framework import generics
from menus.models import MenuItem
from menus import serializers


class MenuItemListAPIView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemListSerializer


class MenuItemDetailAPIView(generics.RetrieveAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemDetailSerializer


class MenuItemUpdateAPIView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemUpdateSerializer


class MenuItemDeleteAPIView(generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemDeleteSerializer
