from django.db import models


class Status(models.Model):
    class State(models.TextChoices):
        PLANNING = ("planning",)
        LIVE = ("live",)
        CANCELLED = ("cancelled",)
        TERMINATED = ("terminated",)

    status = models.fields.CharField(choices=State.choices, max_length=50, unique=True)

    def __str__(self):
        return self.status.capitalize()
