from operator import concat
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
        
    # def save_model(self, request, obj, form, change):
    #     print('here is the object', obj)
    #     print('here is the object', obj)
    #     print('here is the object', obj)
    #     print('here is the object', obj)
    #     print('here is the object', obj)
    #     print('here is the object', obj)
    #     obj.user = request.user
    #     super().save_model(request, obj, form, change)
        
    #     print('here is the object', obj)

    def save(self, commit=True):
        contract = super().save(commit=False)
        related_account = Account.objects.get(id=contract.account.id)
        contract.sales_contact = EpicUser.objects.get(id=related_account.sales_contact.id)
        if contract.__dict__['status']:
            contract.amount = round(contract.__dict__['amount'], 2)
            event = apps.get_model(app_label="event", model_name="Event")
            status = apps.get_model(app_label="status", model_name="Status")
            new_status = status.objects.create(
                status = "planning"
            )
            print('new_status', new_status)
            new_status.save()
            new_event = event.objects.create(
                account = related_account,
                event_status = new_status
            )
            print('new_event', new_event)         
            new_event.save()
        elif contract.__dict__['status'] is None:
            self.amount = round(contract.__dict__['amount'], 2)
        if commit:
            contract.save()
        return contract
        
    # def save(self, *args, **kwargs):
    #     if self.status:
    #         self.amount = round(self.amount, 2)
    #         event = apps.get_model(app_label="event", model_name="Event")
    #         new_event = event.objects.create(
    #             account = self.account
    #         )
    #         self.event = new_event    
    #         new_event.save()
    #     self.amount = round(self.amount, 2)
    #     super(Contract, self).save(*args, **kwargs)



# class ContractChangeForm(forms.ModelForm):
#     """Form to update Contract"""

#     class Meta:
#         model = Contract
#         fields = ("account", "status", "amount", "payment_due")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if user.role == "management":
#             user.is_admin = True
#         else:
#             user.is_admin = False
#         if commit:
#             user.save()
#         return user
