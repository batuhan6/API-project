from django.contrib import admin
from orders import models
from django.utils.translation import gettext_lazy as _


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    fields = ('menu_item', 'quantity', 'unit_price', 'price')
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_crew',
                    'status', 'total', 'date')
    list_filter = ('status', 'date')
    ordering = ('id',)

    inlines = (OrderItemInline,)


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'menu_item',
                    'quantity', 'unit_price', 'price')
    ordering = ('id',)
