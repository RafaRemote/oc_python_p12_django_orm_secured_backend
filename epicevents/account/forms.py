from django import forms
from .models import Account
from users.models import EpicUser

class AccountCreationForm(forms.ModelForm):
    """ Form to create new Account"""
    sales_contact = forms.ModelChoiceField(queryset=EpicUser.objects.filter(role="sales"))
    
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'sales_contact')
