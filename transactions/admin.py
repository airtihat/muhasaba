from django.db import models

class Transaction(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=[('debit', 'مدين'), ('credit', 'دائن')])

    def __str__(self):
        return f"{self.date} - {self.description}"
