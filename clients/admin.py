from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'client_type')  # عرض الأعمدة في القائمة
    list_filter = ('client_type',)                             # الفلترة حسب نوع العميل
    search_fields = ('name', 'phone', 'email')                 # البحث داخل هذه الحقول
