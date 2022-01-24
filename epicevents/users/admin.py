from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import EpicUserChangeForm, EpicUserCreationForm
from users.models import EpicUser


class EpicUserAdmin(BaseUserAdmin):
    form = EpicUserChangeForm
    add_form = EpicUserCreationForm
    list_display = ('username', 'role', 'is_staff', 'is_admin', 'is_superuser')
    list_filter = ('is_admin', 'role')
    fieldsets = (
        (None, {'fields': ('username', 'role')}),
        # ('Personal info', {'fields': ('last_login',)}),
        # ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'role', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(EpicUser, EpicUserAdmin)
