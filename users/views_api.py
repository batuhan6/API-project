from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from users.serializers import serializers_user


class UserDetailAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers_user.UserDetailSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers_user.UserCreateSerializer


class UserLoginAPIView(APIView):
    pass
