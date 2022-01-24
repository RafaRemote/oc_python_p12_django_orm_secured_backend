from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'account',
        'attendees',
        'event_date',
        'event_status'
    )
    list_filter = (
        'event_status',
    )
    def has_add_permission(self, request):
        return False


admin.site.register(Event, EventAdmin)
