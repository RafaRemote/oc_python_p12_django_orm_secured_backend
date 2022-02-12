from django.contrib import admin
from .models import Status
from .forms import StatusForm


class AccountAdmin(admin.ModelAdmin):
    form = StatusForm

    list_display = ("status",)
    list_filter = ("status",)


admin.site.register(Status, AccountAdmin)
