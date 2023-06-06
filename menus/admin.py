from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from menus import models


# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title__icontains',)
    search_help_text = (_('title alanına göre arama yapılabilir'),)
    ordering = ('title',)


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'featured', 'category')
    list_filter = ('category', 'featured')
    search_fields = ('title__icontains',)
    search_help_text = (_('title alanına göre arama yapılabilir'),)
    ordering = ('-price',)


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quantity', 'unit_price', 'price')
    ordering = ('id',)


@admin.register(models.CartMenuItem)
class CartMenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart')
