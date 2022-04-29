"""voicee_pay URL Configuration"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graph.schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path(
        "",
        lambda _: HttpResponse("Welcome to Voicee Pay!<br>-sandy_codes_py"),
        name="index_page",
    ),
    path("admin/", admin.site.urls),
    path(
        "transaction/",
        include(("transaction.urls", "transaction"), namespace="transaction"),
    ),
    path(
        "ussd/",
        include(("ussd.urls", "ussd"), namespace="ussd"),
    ),
    path("api/q/", csrf_exempt(GraphQLView.as_view(schema=schema))),
    path("api/q/explore/", GraphQLView.as_view(graphiql=True, schema=schema))
]
