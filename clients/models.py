from django.db import models

class Client(models.Model):
    CLIENT_TYPES = [
        ('customer', 'عميل'),
        ('supplier', 'مورد'),
    ]

    name = models.CharField(max_length=255, verbose_name="الاسم")
    phone = models.CharField(max_length=20, verbose_name="رقم الجوال")
    email = models.EmailField(verbose_name="البريد الإلكتروني", blank=True, null=True)
    address = models.TextField(verbose_name="العنوان", blank=True, null=True)
    tax_number = models.CharField(max_length=100, verbose_name="الرقم الضريبي", blank=True, null=True)
    client_type = models.CharField(max_length=10, choices=CLIENT_TYPES, verbose_name="نوع العميل")

    class Meta:
        verbose_name = "عميل / مورد"
        verbose_name_plural = "العملاء / الموردين"

    def __str__(self):
        return f"{self.name} ({self.get_client_type_display()})"
