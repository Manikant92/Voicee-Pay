from graphene_django.views import GraphQLView

# using a private view to allow access to only the logged in users


class PrivateGraphQLView(GraphQLView):
    pass
