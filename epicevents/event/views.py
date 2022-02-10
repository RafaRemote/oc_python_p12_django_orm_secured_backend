from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import IsAuthenticated
from epicevents.permissions import IsSupport


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupport]
    http_method_names = ["get", "put", "patch"]

    def get_queryset(self):
        return Event.objects.filter(support_contact=self.request.user).order_by("id")

    def destroy(self):
        print("detroy")
        print("detroy")
        print("detroy")
        print("detroy")
        print("detroy")
        print("detroy")
        print("detroy")
