from django.contrib import admin
from .models import Party  # ✅ اسم النموذج الصحيح

@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'party_type', 'phone', 'email')   # عرض الحقول الرئيسية
    search_fields = ('name', 'phone', 'email')                # إمكانية البحث
    list_filter = ('party_type',)                             # فلتر حسب النوع
    ordering = ('name',)                                      # ترتيب أبجدي حسب الاسم
