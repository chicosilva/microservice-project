from django.db import models
import uuid


class Product(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    qtd_available = models.IntegerField(null=True, blank=True, default=1)
    qtd_total = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.name
