from django.db import models
from accounts.models import Account
from branches.models import Branch

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    attachment = models.FileField(upload_to='expenses/', blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.amount}"
