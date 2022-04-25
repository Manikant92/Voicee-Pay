import graphene
from ussd.models import UssdSession

from transaction.models import Customer, Transaction
from .types import CustomerFields, TransactionFields, UssdSessionFields


class Query(graphene.ObjectType):
    transactions = graphene.List(TransactionFields)
    ussd_sessions = graphene.List(UssdSessionFields)
    customers = graphene.List(CustomerFields)

    def resolve_transactions(self, info):
        return Transaction.objects.all()

    def resolve_ussd_sessions(self, info):
        return UssdSession.objects.all()

    def resolve_customers(self, info):
        return Customer.objects.all()


schema = graphene.Schema(query=Query)
