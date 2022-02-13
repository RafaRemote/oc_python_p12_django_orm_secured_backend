from django.contrib import admin
from .models import Contract
from event.models import Event
from .forms import ContractCreationForm
from datetime import datetime


class ContractAdmin(admin.ModelAdmin):
    form = ContractCreationForm

    list_display = ("pk", "account", "status", "amount", "sales_contact", "payment_due")

    list_filter = (
        "account",
        "sales_contact",
    )

    add_fieldset = (
        (
            None,
            {"classes": ("wide",), "fields": ("account", "status", "sales_contact")},
        ),
    )
    search_fiels = ("account",)
    ordering = ("sales_contact",)
    filter_horizontal = ()

    def delete_queryset(self, request, queryset):
        """
        Search the event related to the contract
        Delete both if time of creation is less than 1 sec.
        """
        contract = Contract.objects.get(pk=queryset[0].id)
        events = Event.objects.filter(account=queryset[0].account)
        contract_timestamp = datetime.timestamp(contract.date_created)
        for event in events:
            if contract_timestamp - datetime.timestamp(event.date_created) < 1:
                contract.delete()
                event.delete()


admin.site.register(Contract, ContractAdmin)
