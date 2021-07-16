from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid', ]

admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Product'