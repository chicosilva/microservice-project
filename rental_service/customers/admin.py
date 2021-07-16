from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'uuid', 'email']

admin.site.register(Customer, CustomerAdmin)

admin.site.site_header = 'Rental'