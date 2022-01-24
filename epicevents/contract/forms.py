from django import forms
from users.models import EpicUser
from account.models import Account
from .models import Contract
from django.apps import apps


class ContractCreationForm(forms.ModelForm):
    """Form to create Contract"""

    class Meta:
        model = Contract
        fields = ("account", "status", "amount", "payment_due")

    def save(self, commit=True):
        contract = super().save(commit=False)
        related_account = Account.objects.get(id=contract.account.id)
        contract.sales_contact = EpicUser.objects.get(
            id=related_account.sales_contact.id
        )
        contract.amount = round(contract.__dict__["amount"], 2)
        if contract.__dict__["status"]:
            event = apps.get_model(app_label="event", model_name="Event")
            status = apps.get_model(app_label="status", model_name="Status")
            new_status = status.objects.filter(status="planning")[0]
            new_event = event.objects.create(
                account=related_account, event_status=new_status
            )
            new_event.save()
        if commit:
            contract.save()
        return contract
