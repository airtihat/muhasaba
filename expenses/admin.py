from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'amount',
        'account',
        'branch',
        'get_short_description',
        'has_attachment',
    )
    search_fields = ('description', 'account__name')
    list_filter = ('date', 'branch', 'account')
    ordering = ('-date',)

    def get_short_description(self, obj):
        if obj.description:
            return (obj.description[:30] + '...') if len(obj.description) > 30 else obj.description
        return "-"
    get_short_description.short_description = 'الوصف'

    def has_attachment(self, obj):
        return bool(obj.attachment)
    has_attachment.boolean = True
    has_attachment.short_description = 'مرفق؟'
