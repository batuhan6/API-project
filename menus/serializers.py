from rest_framework import serializers

from menus.models import MenuItem


class MenuItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class MenuItemDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
