from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account
from event.models import Event
from epicevents.permissions import IsBelongingToAuthorizedGroups
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler("account.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, IsBelongingToAuthorizedGroups]
    http_method_names = ["get", "put", "patch", "post"]
    filterset_fields = ["last_name", "email"]
    search_fields = ["last_name", "email"]
    logger.debug("AccountViewSet allowed http methods: {}".format(http_method_names))

    def get_queryset(self):
        if self.request.user.role == "sales":
            query = Account.objects.filter(sales_contact=self.request.user).order_by(
                "id"
            )
            logger.debug("current user is: {}".format(self.request.user))
            logger.debug("List of Accounts: {}".format(query))
            return query
        else:
            supported_events = Event.objects.filter(support_contact=self.request.user)
            supported_accounts_ids = [event.account.id for event in supported_events]
            queryset = Account.objects.filter(id__in=supported_accounts_ids)
        return queryset
