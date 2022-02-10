from rest_framework.permissions import BasePermission
from event.models import Event
from contract.models import Contract


class IsBelongingToAuthorizedGroups(BasePermission):
    """Set permission based on group belonging"""

    authorized_groups = ["sales", "support"]

    def has_permission(self, request, view):
        support_forbidden = ["update", "create"]
        if view.action == "retrieve" and request.user.role == "support":
            all_events = Event.objects.filter(support_contact=request.user.id)
            req_user_accounts = [
                str(account_holder.account.id) for account_holder in all_events
            ]
            if view.kwargs["pk"] in req_user_accounts:
                return True
            else:
                return False
        elif (view.action in support_forbidden) and request.user.role == "support":
            return False
        elif request.user.role in self.authorized_groups:
            return True
        else:
            return False


class IsSales(BasePermission):
    """Set permission based on group belonging"""

    def has_permission(self, request, view):

        if view.action == "retrieve" and request.user.role == "sales":
            contract_sales_contact = Contract.objects.get(
                pk=view.kwargs["pk"]
            ).sales_contact.id
            if request.user.id == contract_sales_contact:
                return True
            else:
                return False

        if request.user.role == "sales":
            return True
        else:
            return False


class IsContractSalesContact(BasePermission):
    """Set permission based on group belonging"""

    def has_permission(self, request, view):
        actions = ["put", "patch"]
        if view.action in actions and request.user.role == "sales":
            contract = Contract.objects.get(pk=view.kwargs["pk"])
            print(contract.sales_contact)
            print(request.user.id)
            if contract.sales_contact == request.user.id:
                return True
            else:
                return False


class IsSupport(BasePermission):
    """Set permission based on group belonging"""

    def has_permission(self, request, view):
        if view.action == "retrieve" and request.user.role == "support":
            event = Event.objects.get(pk=view.kwargs["pk"])
            if request.user.id == event.support_contact.id:
                return True
            else:
                return False

        if request.user.role == "support":
            return True
        else:
            return False
