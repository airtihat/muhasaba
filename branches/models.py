from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    manager = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
