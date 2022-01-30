from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from .forms import EpicUserChangeForm, EpicUserCreationForm
from users.models import EpicUser


class EpicUserAdmin(BaseUserAdmin):
    form = EpicUserChangeForm
    add_form = EpicUserCreationForm
    list_display = ("username", "role", "is_staff", "is_admin", "is_superuser")
    list_filter = ("is_admin", "role", "groups")
    fieldsets = ((None, {"fields": ("username", "role")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "role", "password1", "password2"),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ()


admin.site.register(EpicUser, EpicUserAdmin)
admin.site.register(Permission)


# can_add_account = Permission.objects.get(name="Can add account")
# can_add_event = Permission.objects.get(name="Can add event")

# epicuser = EpicUser.object.get(all)


# sales_team_permission = [
#     can_add_account,
#     can_add_event
# ]

# for perm in sales_team_permission:
#     sales_team.permissions.add(perm)
