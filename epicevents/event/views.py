from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import IsAuthenticated
from epicevents.permissions import IsSupport
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("event.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class EventViewSet(viewsets.ModelViewSet):

    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsSupport]
    http_method_names = ["get", "put", "patch"]

    logger.info("EventViewSet allowed HTTP methods {}".format(http_method_names))

    def get_queryset(self):
        return Event.objects.filter(support_contact=self.request.user).order_by("id")
