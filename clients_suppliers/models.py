from django.db import models

class Party(models.Model):
    PARTY_TYPES = [
        ('client', 'عميل'),
        ('supplier', 'مورد'),
    ]

    name = models.CharField(max_length=255, verbose_name='الاسم')
    party_type = models.CharField(max_length=10, choices=PARTY_TYPES, verbose_name='النوع')
    phone = models.CharField(max_length=20, verbose_name='رقم الجوال')
    email = models.EmailField(blank=True, null=True, verbose_name='البريد الإلكتروني')
    address = models.TextField(blank=True, null=True, verbose_name='العنوان')

    def __str__(self):
        return f"{self.name} ({self.get_party_type_display()})"

    class Meta:
        verbose_name = "طرف"
        verbose_name_plural = "الأطراف"
        ordering = ['name']
