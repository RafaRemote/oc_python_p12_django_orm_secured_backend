import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import EpicUser
from account.models import Account


class Contract(models.Model):
    sales_contact = models.ForeignKey(EpicUser, blank=True, null=True, on_delete=models.SET_NULL, limit_choices_to={"role": "sales"})
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name="signed")
    amount = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10000000)])
    payment_due = models.DateField(validators=[MinValueValidator(datetime.date.today)])

    def __str__(self):
        return f"Contract for Account ==> {self.account} Sales Contact ==> {self.sales_contact}"
