
from django.db import models

class SystemSettings(models.Model):
    fiscal_year_start = models.DateField(verbose_name='بداية السنة المالية')
    fiscal_year_end = models.DateField(verbose_name='نهاية السنة المالية')
    default_currency = models.CharField(max_length=10, verbose_name='العملة')
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='نسبة الضريبة')
