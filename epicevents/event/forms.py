from django import forms
from .models import Event


class EventChangeForm(forms.ModelForm):
    """Form to update Event"""

    class Meta:
        model = Event
        fields = ('attendees', 'support_contact', 'event_date')
