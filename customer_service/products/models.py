from django.db import models
import uuid


class Product(models.Model):

    uuid = models.CharField(default=uuid.uuid4, editable=False, max_length=200, db_index=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
