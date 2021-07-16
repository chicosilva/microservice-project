# Generated by Django 3.2.5 on 2021-07-16 11:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.CharField(db_index=True, default=uuid.uuid4, editable=False, max_length=200),
        ),
    ]
