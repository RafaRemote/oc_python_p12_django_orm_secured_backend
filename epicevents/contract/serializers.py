from rest_framework import serializers

from .models import Contract
from account.models import Account


class ContractSerializer(serializers.ModelSerializer):
    sales_contact_name = serializers.SerializerMethodField()
    sales_contact = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ["account", "amount", "payment_due"]
        ordering = ["id"]
        new_fields = [
            "id",
            "sales_contact_name",
            "sales_contact",
            "status",
            "account_name",
        ]
        for i in new_fields:
            fields.append(i)

    def get_sales_contact(self, obj):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        obj.sales_contact = user
        return user.id

    def get_sales_contact_name(self, obj):
        return self.context.get("request").user.username

    def get_account_name(self, obj):
        f_name = Account.objects.get(pk=obj.account.id).first_name
        l_name = Account.objects.get(pk=obj.account.id).last_name
        return f"{f_name} {l_name}"
