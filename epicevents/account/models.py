from django.db import models
from users.models import EpicUser


class Account(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        EpicUser,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to={"role": "sales"},
    )

    def __str__(self):
        return self.first_name.capitalize() + " " + self.last_name.capitalize()
