from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    descriptions = models.TextField(max_length=250, verbose_name=_('Açıklamalar'),
                                    help_text=_('Açıklamalar'), null=True, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Rol')
        verbose_name_plural = _('Roller')

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT,
                             null=True, blank=True)
