import os
import django

def load():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "epicevents.settings")
    django.setup()
    from status.models import Status

    list_status = ["planning", "live", "terminated", "cancelled"]
    
    [Status.objects.create(status=i) for i in list_status]

if __name__ == '__main__':
    load()