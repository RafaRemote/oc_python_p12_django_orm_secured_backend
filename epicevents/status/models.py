from tabnanny import verbose
from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.status.capitalize()

