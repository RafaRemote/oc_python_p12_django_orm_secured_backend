from django import forms
from .models import Status
from event.models import Event

from django.apps import apps


class StatusForm(forms.ModelForm):
    """Form to handle Status"""
    
    
    class Meta:
        model = Status
        fields = ("status",)
