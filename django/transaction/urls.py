from django.urls import path

from .views import dialogflow_webhook, transaction_home
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path(
        "dialogflow_webhook", csrf_exempt(dialogflow_webhook), name="dialogflow_webhook"
    ),
    path("home", transaction_home, name="home"),
]
