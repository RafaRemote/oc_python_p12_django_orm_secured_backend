import datetime
from django.db import models
from account.models import Account
from users.models import EpicUser
from status.models import Status
from django.core.validators import MaxValueValidator, MinValueValidator

class Event(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    support_contact = models.ForeignKey(EpicUser, default=None, null=True, on_delete=models.SET_DEFAULT, limit_choices_to="support")
    attendees = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10000),
            MinValueValidator(1)
        ])
    event_date = models.DateField(null=True, blank=True, validators=[MinValueValidator(datetime.date.today)])
    notes = models.TextField(null=True, blank=True)
    event_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    def __str__(self):
        return (f"EVENT for Account ==> {self.account} Support ==> {self.support_contact}.")
