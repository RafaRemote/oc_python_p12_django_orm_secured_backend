from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class EpicUserManager(BaseUserManager):
    def create_user(self, username, role, password):
        """
        Creates and saves User with given username, role and password.
        """
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

    def create_superuser(self, username, role, password):
        """
        Creates and saves superuser using given username, role and password
        """
        user = self.create_user(
            username,
            password=password,
            role=role,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class EpicUser(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        MANAGEMENT = ("management",)
        SUPPORT = ("support",)
        SALES = "sales"

    username = models.CharField(max_length=150, unique=True, null=False, blank=False)
    role = models.fields.CharField(choices=Role.choices, max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role"]

    objects = EpicUserManager()

    def __str__(self):
        return self.username.capitalize()
