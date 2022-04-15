import json
import logging
from django.http.response import JsonResponse, HttpResponse
from transaction.utils import process_dialogflow_webhook

logger = logging.getLogger("django")


def dialogflow_webhook(request):
    if request.method == "POST":
        body_unicode = request.body.decode("utf-8")

        # this gives use the entire content in json
        body = json.loads(body_unicode)

        process_dialogflow_webhook(body)

        return JsonResponse(
            {
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                "Thanks submitting your payment request, we'll let you know once the request is processed"
                            ]
                        }
                    }
                ]
            }
        )
    else:
        return HttpResponse("URL is valid.<br>Send a post request to this URL")


def transaction_home(request):
    logger.info("Test URL successfly triggered!!")
    return HttpResponse("This is a test URL for transation")
