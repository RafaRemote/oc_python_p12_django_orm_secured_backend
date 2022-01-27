from django.contrib import admin
from .models import Event
from .forms import EventChangeForm


class EventAdmin(admin.ModelAdmin):
    form = EventChangeForm

    list_display = ("pk", "account", "attendees", "event_date", "event_status", "support_contact")

    list_filter = ("event_status", "support_contact", "event_status")

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

    def pk(self, obj):
        return f"Event {str(obj.pk)}"
    
    # pk.short_description = "Event"

admin.site.register(Event, EventAdmin)
