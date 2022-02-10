from rest_framework import serializers

from .models import Account
from users.models import EpicUser


class AccountSerializer(serializers.ModelSerializer):
    sales_contact_name = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [field.name for field in model._meta.fields]
        fields.append("sales_contact_name")

    def get_sales_contact_name(self, obj):
        return EpicUser.objects.get(pk=obj.sales_contact.id).username
