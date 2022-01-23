from django import forms
from .models import EpicUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    """Form to create new users. Includes all required fields, plus repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = EpicUser
        fields = ("username", "role")

    def clean_password2(self):
        # Check if password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.role == "management":
            user.is_superuser = True
            user.is_admin = True
            user.is_staff = True
        else:
            user.is_admin = False
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Form to update users. Includes all fields on
    user, but replaces password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = EpicUser
        fields = ("username", "role")

    def save(self, commit=True):
        user = super().save(commit=False)
        if user.role == "management":
            user.is_admin = True
        else:
            user.is_admin = False
        if commit:
            user.save()
        return user
