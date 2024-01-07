from rest_framework import generics, viewsets, status
from orders.models import Order, OrderItem
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from orders import serializers, order_serializers
from users.permissions.role_permissions import RolePermission
from users.permissions.user_permissions import UserPermission


class OrderListOrCreateAPIViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = order_serializers.OrderListSerializer
    create_serializer_class = order_serializers.OrderCreateSerializer
    permission_classes = [UserPermission]
    perm_slug = "orders.order"

    def retrieve(self, request, *args, **kwargs):
        try:
            if request.user.role.slug not in [""]:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except AttributeError:
            obj_user = self.get_object().user
            if obj_user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return super().retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager", "delivery-crew"]:
                serializer = self.serializer_class(self.queryset, many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)

        except AttributeError:
            # Customer ise buraya giricek
            queryset = self.queryset.filter(user=request.user)
            print(queryset.query)
            serializer = self.serializer_class(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        try:
            if request.user.role.slug in ["manager", "delivery-crew"]:  # customer i nasıl ekleyecem
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

