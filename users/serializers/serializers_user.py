from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
