from django.contrib import admin
from .models import Contract
from .forms import ContractCreationForm
from django.utils.html import format_html


class ContractAdmin(admin.ModelAdmin):    
    form = ContractCreationForm
    
    list_display = (
        'account',
        'status',
        'amount',
        'sales_contact',
        'payment_due'
        )

    list_filter = (
                   'account',
                   'sales_contact',
                   )
    
    add_fieldset = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("account", "status", "sales_contact")
                
            },
        ),
    )
    search_fiels = ("account",)
    ordering = ("sales_contact",)
    filter_horizontal = ()

admin.site.register(Contract, ContractAdmin)
