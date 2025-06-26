from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان التقرير')
    content = models.TextField(verbose_name='محتوى التقرير')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self):
        return self.title
