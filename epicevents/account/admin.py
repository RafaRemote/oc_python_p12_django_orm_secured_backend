from django.contrib import admin
from .models import Account
from .forms import AccountCreationForm


class AccountAdmin(admin.ModelAdmin):
    form = AccountCreationForm

    list_display = (
        "first_name",
        "last_name",
        "sales_contact",
        "date_created",
        "date_updated",
    )
    list_filter = ("sales_contact",)

    add_fieldset = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "sales_contact"),
            },
        ),
    )
    search_fiels = ("first_name",)
    ordering = ("first_name",)
    filter_horizontal = ()


admin.site.register(Account, AccountAdmin)
