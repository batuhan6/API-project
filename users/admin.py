from django.contrib import admin
from users import models
from django.utils.translation import gettext_lazy as _


# Register your models here.

@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'username', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first__icontains', 'last_name__icontains',
                     'username__icontains', 'email__icontains')
    search_help_text = (_('''Bu alanda first_name, last_name, 
                          username, email alanlarına göre arama 
                          yapabilirsiniz'''))
    ordering = ('username',)


@admin.register(models.UserRole)
class CustomUserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',
                    'status', 'created_date', 'updated_date')
    list_filter = ('status', 'created_date', 'updated_date')
    search_fields = ('name__icontains',)
    ordering = ('id',)


