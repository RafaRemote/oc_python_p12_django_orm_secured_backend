from email.policy import default
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class EpicUserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        """Creates and saves user with given username and role"""

        if not role:
            raise ValueError("Users must have a role")
        user = self.model(username=username, role=role)
        if user.role == "management":
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
            user.set_password(password)
            user.save(using=self._db)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """Creates and saves superuser with given username and password"""
        user = self.create_user(
            username,
            password=password,
            role="management",
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EpicUser(AbstractBaseUser):
    class Department(models.TextChoices):
        MANAGEMENT = ("management",)
        SUPPORT = ("support",)
        SALES = "sales"
    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    role = models.fields.CharField(choices=Department.choices, max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = EpicUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['']

    def __str__(self):
        return self.username.capitalize()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
