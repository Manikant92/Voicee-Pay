from django.http import HttpResponse
import logging

from transaction.models import Customer
from .utils import execute_action
from .models import UssdSession

logger = logging.getLogger("django")


def af_webhook(request):
    if request.method == "POST":
        logger.info("Triggered Africa Talking Webhook!")
        response = "END ."
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

            # method_name = get_method_name_from_user_input(user_input)
            # callable_action_method: Callable = globals()[method_name]
            # logger.info(f"Executing - {callable_action_method.__name__}")
            response = execute_action(user_input, customer_obj)

            # # initial trigger from USSD service
            # if user_input == "":
            #     if customer_obj:
            #         response = USSD_RESPONSES["select_language"]
            #     else:
            #         response = USSD_RESPONSES["no_account_error"]
            # TODO: create a method which takes in user_input and returns the method to call and cleaned user_input
            # elif user_input == "1":
            #     response = USSD_RESPONSES[
            #         "balance_response"
            #     ] + check_balance_with_phone_number(user_phone)

            # elif user_input == "2":
            #     response = USSD_RESPONSES["transfer_money"]

            # elif user_input == "3":
            #     response = USSD_RESPONSES["end"]

            # elif user_input.startswith("2*"):
            #     # removed since we have this from the previous response
            #     user_input = user_input.replace("2*", "")
            #     response = transfer_money(user_input, user_phone)

        except:
            logger.exception("There is an error while responding!")

        logger.info(f"sending response - {response}")

        return HttpResponse(response, content_type="text/plain")

    else:
        return HttpResponse(
            "This is the Africa Talking webhook URL. Send a post request"
        )
