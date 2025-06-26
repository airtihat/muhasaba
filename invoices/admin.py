from django.contrib import admin
from .models import Invoice, InvoiceItem

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['number', 'customer', 'total', 'created_at', 'status']
    search_fields = ['number', 'customer__name']
    list_filter = ['status', 'created_at']
    ordering = ['-created_at']

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ['invoice', 'description', 'quantity', 'unit_price', 'subtotal']
    search_fields = ['description']
    list_filter = ['invoice']
