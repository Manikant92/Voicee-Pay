import graphene
from graphene_django.types import DjangoObjectType
from ussd.models import UssdSession
from transaction.models import Customer, PaymentRequest, Transaction


class TransactionFields(DjangoObjectType):
    class Meta:
        model = Transaction
        fields = (
            "created_at",
            "transaction_id",
            "sender_account",
            "receiver_account",
            "amount",
            "status",
        )


class UssdSessionFields(DjangoObjectType):
    class Meta:
        model = UssdSession
        fields = ("created_at", "session_id")


class CustomerFields(DjangoObjectType):
    class Meta:
        model = Customer
        fields = (
            "name",
            "email",
            "is_active",
        )
