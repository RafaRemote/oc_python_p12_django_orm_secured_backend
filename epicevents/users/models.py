from multiprocessing.managers import BaseManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    
        
    def create_superuser(self, user_name, role, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(user_name, role, password, **other_fields)
    
    def create_user(self, user_name, role, password, **other_fields):
        user = self.model(user_name=user_name, role=role, **other_fields)
        user.set_password(password)
        user.save()
        return user

    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        MANAGEMENT = 'Management'
        SUPPORT = 'Support'
        SALES = 'Sales'
    
    user_name = models.CharField(max_length=150, unique=True)
    role = models.fields.CharField(choices=Role.choices, max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    if role == "Management":
        is_staff = True
        
    objects = CustomUserManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.user_name

 