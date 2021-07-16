from django.db import models
import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .service import produce_customer


class Customer(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=Customer)
def add_customer_to_qeue(sender, instance, **kwargs):
    produce_customer(instance)
    