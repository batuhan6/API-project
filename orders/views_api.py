from rest_framework import generics, viewsets, status
from orders.models import Order, OrderItem
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from orders import serializers
from users.permissions.role_permissions import RolePermission
from users.permissions.user_permissions import UserPermission

#
# class OrderItemListOrCreateAPIViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     list_serializer_class = serializers.OrderItemListSerializer
#     create_serializer_class = serializers.OrderItemCreateSerializer
#     permission_classes = [UserPermission]
#     perm_slug = "orders.orderitem"
#
#     def list(self, request, *args, **kwargs):
#         try:
#             if request.user.role.slug in ["manager", "delivery-crew"]:
#                 serializer = self.list_serializer_class(self.queryset, many=True)
#                 return Response(serializer.data)
#             return Response(status=status.HTTP_403_FORBIDDEN)
#         except AttributeError:
#             serializer = self.list_serializer_class(self.queryset, many=True)
#             return Response(serializer.data)
#
#     def create(self, request, *args, **kwargs):
#         # try:
#         if request.user.role.slug in ["manager", "delivery-crew"]:  # customer i nasıl ekleyecem
#             serializer = self.create_serializer_class(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #     else:
#     #         raise APIException("No permission")
#     # except AttributeError:
#     #     raise APIException("No permission")
#
#
#
# class OrderDetailUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderItemDetailSerializer
#     perm_slug = "orders.orderitem"
#     permission_classes = [UserPermission]
#
#     def retrieve(self, request, *args, **kwargs):
#         try:
#             if request.user.role.slug in ["delivery-crew"]:
#                 return super().retrieve(request, *args, **kwargs)
#             else:
#                 raise APIException("No permission")
#         except AttributeError:
#             return super().retrieve(request, *args, **kwargs)
#
#     def update(self, request, *args, **kwargs):
#         try:
#             if request.user.role.slug in ["delivery-crew"]:
#                 return super().update(request, *args, **kwargs)
#             else:
#                 raise APIException("No permission")
#         except AttributeError:
#             raise APIException("No permission")
#
#     def destroy(self, request, *args, **kwargs):
#         try:
#             if request.user.role.slug in ["manager"]:
#                 return super().destroy(request, *args, **kwargs)
#             else:
#                 raise APIException("No permission")
#         except AttributeError:
#             raise APIException("No permission")
#
#
#









###############################################################################################


#
# class OrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderListSerializer
#
#
# class OrderDetailAPIView(generics.RetrieveAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderDetailSerializer
#
#
# class OrderUpdateAPIView(generics.UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderUpdateSerializer
#
#
# class OrderDeleteAPIView(generics.DestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderDeleteSerializer

