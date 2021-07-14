from django.db import models
import uuid


class Order(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=70)
    discount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    
    def __str__(self):
        return self.name


class OrderItem(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    qtd = models.IntegerField(null=True, blank=True, default=1)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    
    
    def __str__(self):
        return self.name
