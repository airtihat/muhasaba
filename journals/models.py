from django.db import models

class JournalEntry(models.Model):
    date = models.DateField(verbose_name='التاريخ')
    description = models.TextField(verbose_name='الوصف')
    created_at = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.description[:20]}..."

class JournalLine(models.Model):
    entry = models.ForeignKey(JournalEntry, related_name='lines', on_delete=models.CASCADE)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.account} | D:{self.debit} C:{self.credit}"
