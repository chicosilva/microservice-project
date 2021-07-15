from django.contrib import admin
from .models import Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ['total']

class PaymentInline(admin.TabularInline):
    model = Payment
    

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
        PaymentInline,
    ]

    list_display = ['customer', 'total', 'balance']
    readonly_fields = ['total', 'balance']

admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
