from django import forms
from .models import Status


class StatusForm(forms.ModelForm):
    """Form to handle Status"""

    class Meta:
        model = Status
        fields = ("status",)
