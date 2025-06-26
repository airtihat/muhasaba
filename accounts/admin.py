from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type', 'parent', 'is_active')  # ✅
    list_filter = ('type', 'is_active')                             # ✅
    search_fields = ('name', 'code')
    ordering = ('code',)
