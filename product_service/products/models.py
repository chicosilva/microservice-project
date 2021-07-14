from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    qtd_available = models.IntegerField(null=True, blank=True, default=1)
    qtd_total = models.IntegerField(null=True, blank=True, default=1)
    
    def __str__(self):
        return self.name
