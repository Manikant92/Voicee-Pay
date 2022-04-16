from django.http import HttpResponse
import logging

from .utils import check_balance_with_phone_number
from .constants import USSD_RESPONSES
from .models import UssdSession

logger = logging.getLogger("django")


def af_webhook(request):
    if request.method == "POST":
        logger.info("Triggered Africa Talking Webhook!")
        response = ""
        try:

            session_id = request.POST["sessionId"]
            # get phone number without country code
            user_mobile = request.POST["phoneNumber"].replace("+91", "")
            user_input = request.POST["text"]

            UssdSession.objects.create(
                session_id=session_id, user_mobile=user_mobile, user_input=user_input
            )

            logger.info("Successfully recorded session details!")

            # initial trigger from USSD service
            if user_input == "":
                response = USSD_RESPONSES["initial"]
            elif user_input == "1":
                response = USSD_RESPONSES[
                    "balance_response"
                ] + check_balance_with_phone_number(user_mobile)
            elif user_input == "2":
                pass
            elif user_input == "3":
                response = USSD_RESPONSES["end"]

        except:
            logger.exception("There is an error while responding!")

        logger.info(f"sending response - {response}")

        return HttpResponse(response, content_type="text/plain")

    else:
        return HttpResponse(
            "This is the Africa Talking webhook URL. Send a post request"
        )
