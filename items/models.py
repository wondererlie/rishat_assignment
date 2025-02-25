from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("-id",)
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

        db_table = "items"

    def __str__(self):
        return self.name
