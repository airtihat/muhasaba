from django.db import models

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('asset', 'أصل'),
        ('liability', 'التزام'),
        ('equity', 'حقوق ملكية'),
        ('income', 'إيراد'),
        ('expense', 'مصروف'),
    ]

    name = models.CharField(max_length=255, verbose_name='اسم الحساب')
    code = models.CharField(max_length=20, unique=True, verbose_name='رمز الحساب')
    type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, verbose_name='نوع الحساب')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    is_active = models.BooleanField(default=True, verbose_name='نشط')

    def __str__(self):
        return f"{self.code} - {self.name}"
