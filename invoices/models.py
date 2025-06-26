from django.db import models
from clients.models import Client
from branches.models import Branch  # ✅ الصحيح

class Invoice(models.Model):
    STATUS_CHOICES = [
        ('paid', 'مدفوعة'),
        ('unpaid', 'غير مدفوعة'),
        ('partial', 'مدفوعة جزئيًا'),
    ]

    number = models.CharField(max_length=50, unique=True, verbose_name="رقم الفاتورة")
    date = models.DateField(verbose_name="تاريخ الفاتورة")
    customer = models.ForeignKey(Client, on_delete=models.CASCADE, limit_choices_to={'client_type': 'customer'}, verbose_name="العميل")
    total = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="الإجمالي")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="الحالة")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="الفرع")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")  # ✅ مضافة

    def __str__(self):
        return f"فاتورة #{self.number}"

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items', verbose_name="الفاتورة")
    description = models.CharField(max_length=255, verbose_name="الوصف")
    quantity = models.PositiveIntegerField(verbose_name="الكمية")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الوحدة")
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="الإجمالي الفرعي")

    def __str__(self):
        return f"{self.description} - {self.invoice.number}"
