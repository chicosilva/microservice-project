# Generated by Django 3.2.5 on 2021-07-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210715_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='return_date',
            new_name='return_at',
        ),
    ]
