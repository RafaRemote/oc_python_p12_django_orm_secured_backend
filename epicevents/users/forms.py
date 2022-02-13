from django import forms
from .models import EpicUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .groups import dispatch_user
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("user_form.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class EpicUserCreationForm(forms.ModelForm):
    """Form to save user from form, dispatched in respective groups"""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = EpicUser
        fields = ("username", "password", "role", "is_active", "is_admin")

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.role == "management":
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_admin = False
            user.is_superuser = False

        if commit:
            user.save()
        dispatch_user(user)
        return user
