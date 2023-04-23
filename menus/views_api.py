from rest_framework import generics, viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from menus.models import MenuItem
from menus import serializers
from users.permissions.user_permissions import UserPermission


class MenuItemListOrCreateAPIViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    list_serializer_class = serializers.MenuItemListSerializer
    create_serializer_class = serializers.MenuItemCreateSerializer
    permission_classes = [UserPermission]
    perm_slug = "menus.menuitem"

    def list(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager", "delivery-crew"]:
                serializer = self.list_serializer_class(self.queryset, many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except AttributeError:
            serializer = self.list_serializer_class(self.queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                serializer = self.create_serializer_class(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise APIException("No permission")
        except AttributeError:
            raise APIException("No permission")


class MenuItemDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = serializers.MenuItemDetailSerializer
    perm_slug = "menus.menuitem"
    permission_classes = [UserPermission]

    def retrieve(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager", "delivery-crew"]:
                return super().retrieve(request, *args, **kwargs)
            else:
                raise APIException("No permission")
        except AttributeError:
            return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                return super().update(request, *args, **kwargs)
            else:
                raise APIException("No permission")
        except AttributeError:
            raise APIException("No permission")

    def destroy(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager"]:
                return super().destroy(request, *args, **kwargs)
            else:
                raise APIException("No permission")
        except AttributeError:
            raise APIException("No permission")



