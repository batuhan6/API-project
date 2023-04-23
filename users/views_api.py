from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from users.permissions.role_permissions import RolePermission
from users.serializers import serializers_user
from users.permissions.user_permissions import UserPermission


class ManagerListOrCreateAPIViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers_user.UserListSerializer
    list_serializer_class = serializers_user.UserListSerializer
    create_serializer_class = serializers_user.UserCreateSerializer
    permission_classes = [UserPermission]
    perm_slug = "users.customuser"

    def list(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                serializer = self.list_serializer_class(self.queryset, many=True)
                return Response(serializer.data)
        except AttributeError:
            serializer = self.list_serializer_class(self.queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                serializer = self.create_serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save(groups=[1])
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise APIException("No permission")
        except AttributeError:
            raise APIException("No permission")


class DeliveryCrewListOrCreateAPIViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    list_serializer_class = serializers_user.UserListSerializer
    create_serializer_class = serializers_user.UserCreateSerializer
    permission_classes = [UserPermission]
    perm_slug = "users.customuser"

    def list(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                serializer = self.list_serializer_class(self.queryset, many=True)
                return Response(serializer.data)
        except AttributeError:
            serializer = self.list_serializer_class(self.queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                serializer = self.create_serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save(groups=[2])
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise APIException("No permission")
        except AttributeError:
            raise APIException("No permission")


class ManagerDeleteAPIView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers_user.UserDeleteSerializer
    perm_slug = "users.customuser"
    permission_classes = [RolePermission, UserPermission]
    accessible_roles = ['manager']

    def delete(self, request, *args, **kwargs):
        if 1 in [item.get('id') for item in self.get_object().groups.only("id").all().values()]:
            return super().delete(request, *args, **kwargs)
        else:
            raise APIException("Due to user is not being in this group it can not be deleted.")


class DeliveryCrewDeleteAPIView(generics.DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers_user.UserDeleteSerializer
    perm_slug = "users.customuser"
    permission_classes = [RolePermission, UserPermission]
    accessible_roles = ['manager']

    def delete(self, request, *args, **kwargs):
        if 2 in [item.get('id') for item in self.get_object().groups.only("id").all().values()]:
            return super().delete(request, *args, **kwargs)
        else:
            raise APIException("Due to user is not being in this group it can not be deleted.")
