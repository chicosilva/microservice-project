from django.db import models
import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Order(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    status = models.CharField(max_length=70)
    discount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    downpayment = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    deliveryfee = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    latefee = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    return_at = models.DateTimeField(editable=False, null=True, blank=True,)
    
    def __str__(self):
        return self.customer.name

    def get_total(self):
        
        total = 0
        for item in self.get_itens.all():
            total += item.product.price * item.qtd

        return total

    def get_total_payments(self):

        total = 0

        for item in self.get_payments.all():
            total = total + item.amount
        
        return total

    def adjust_balance(self):
        
        if self.balance != self.get_total() - self.get_total_payments():
            self.balance = self.get_total() - self.get_total_payments()
    
    def adjust_total(self):

        if self.total != self.get_total():
            self.total = self.get_total()
        
        return self.total


class OrderItem(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='get_itens')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    qtd = models.IntegerField(null=True, blank=True, default=1)
    total = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True,)
    
    def __str__(self):
        return self.product.name


class Payment(models.Model):
    
    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='get_payments')
    payment_type = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_date = models.DateTimeField(editable=False)

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=OrderItem, dispatch_uid="update_stock_count")
def update_prices(sender, instance, **kwargs):
    
    Order.objects.\
        filter(pk=instance.order.pk).\
        update(total=instance.order.adjust_total())
    
    OrderItem.objects.\
        filter(pk=instance.pk).\
        update(total=instance.qtd * instance.product.price)

    #instance.adjust_balance()
    #instance.adjust_total()
    