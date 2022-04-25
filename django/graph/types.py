import graphene
from graphene_django.types import DjangoObjectType
from transaction.models import Transaction


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
