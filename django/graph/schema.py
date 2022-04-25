import graphene

from transaction.models import Transaction
from .types import TransactionFields


class Query(graphene.ObjectType):
    transactions = graphene.List(TransactionFields)

    def resolve_transactions(self, info):
        return Transaction.objects.all()


schema = graphene.Schema(query=Query)
