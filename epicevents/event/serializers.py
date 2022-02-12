from rest_framework import serializers

from .models import Event
from users.models import EpicUser
from .models import Account


class EventSerializer(serializers.ModelSerializer):
    support_contact_name = serializers.SerializerMethodField()
    account_owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [field.name for field in model._meta.fields]
        fields.append("support_contact_name")
        fields.append("account_owner_name")

    def get_support_contact_name(self, obj):
        return EpicUser.objects.get(pk=obj.support_contact.id).username

    def get_account_owner_name(self, obj):
        f_name = Account.objects.get(pk=obj.account.id).first_name
        l_name = Account.objects.get(pk=obj.account.id).last_name
        return f"{f_name} {l_name}"
