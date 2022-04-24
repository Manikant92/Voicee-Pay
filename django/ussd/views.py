from django.http import HttpResponse
import logging

from transaction.models import Customer
from .utils import execute_action
from .models import UssdSession

logger = logging.getLogger("django")


def af_webhook(request):
    if request.method == "POST":
        logger.info("Triggered Africa Talking Webhook!")
        response = "END Invalid Code."
        try:

            session_id = request.POST["sessionId"]
            # get phone number without country code
            user_phone = request.POST["phoneNumber"].replace("+91", "")
            user_input = request.POST["text"]

            UssdSession.objects.create(
                session_id=session_id, user_phone=user_phone, user_input=user_input
            )

            logger.info("Successfully recorded session details!")

            customer_obj: Customer = Customer.objects.filter(
                phone_number=user_phone
            ).first()

            # this is the place where the code is mapped to an action
            response = execute_action(user_input, customer_obj)

        except:
            logger.exception("There is an error while responding!")

        logger.info(f"sending response - {response}")

        return HttpResponse(response, content_type="text/plain")

    else:
        return HttpResponse(
            "This is the Africa Talking webhook URL. Send a post request"
        )
