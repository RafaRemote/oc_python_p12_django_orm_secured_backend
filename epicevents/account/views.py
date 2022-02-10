from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account
from event.models import Event
from epicevents.permissions import IsBelongingToAuthorizedGroups
from rest_framework.permissions import IsAuthenticated


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, IsBelongingToAuthorizedGroups]
    http_method_names = ["get", "put", "patch", "post"]

    def get_queryset(self):
        print("get_queryset")
        if self.request.user.role == "sales":
            return Account.objects.filter(sales_contact=self.request.user).order_by(
                "id"
            )
        else:
            supported_events = Event.objects.filter(support_contact=self.request.user)
            print("self.requser", self.request.user)
            print("supported_evens", supported_events)
            if len(supported_events) > 0:
                supported_accounts_ids = [
                    event.account.id for event in supported_events
                ]
        queryset = Account.objects.filter(id__in=supported_accounts_ids)
        return queryset
