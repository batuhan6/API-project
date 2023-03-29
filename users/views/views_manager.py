from rest_framework import generics
from django.contrib.auth import get_user_model
from users.serializers.serializers_manager import ManagerListSerializer


class ManagerListAPIView(generics.ListAPIView):
    queryset = get_user_model()
    serializer_class = ManagerListSerializer
