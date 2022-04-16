from django.urls import path

from .views import af_webhook
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("webhook", csrf_exempt(af_webhook), name="af_webhook"),
]
