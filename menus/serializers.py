from rest_framework import serializers

from menus.models import MenuItem, Cart, CartMenuItem


class MenuItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


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


class CartMenuItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartMenuItem
        fields = "__all__"


class CartListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = "__all__"

    def get_items(self, obj):
        cart_items = obj.cart_items.all()
        serializer = CartMenuItemListSerializer(cart_items, many=True)
        return serializer.data


class CartMenuItemDetailSerializer(serializers.ModelSerializer):
    menu_item = MenuItemDetailSerializer()

    class Meta:
        model = CartMenuItem
        exclude = ('cart',)


class CartDetailSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()

    def get_cart_items(self, obj):
        data = obj.cart_items.all()
        print(data)
        serializer = CartMenuItemDetailSerializer(data, many=True)
        return serializer.data

    class Meta:
        model = Cart
        fields = "__all__"


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
