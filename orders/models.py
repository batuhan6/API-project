from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name="delivery_crew",
                                      null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(db_index=True)

    def __str__(self) -> str:
        return str(self.status)


class OrderItem(models.Model):
    order = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    menu_item = models.ForeignKey("menus.MenuItem", on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'menu_item')

    def __str__(self) -> str:
        return str(self.quantity)
