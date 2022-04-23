from django.http import JsonResponse
from transaction.constants import DIALOGFLOW_RESPONSE_TEMPLATE
from transaction.models import BankAccount, PaymentRequest
import logging

logger = logging.getLogger("django")


def process_dialogflow_webhook(body):

    query_result = body["queryResult"]

    parameters = query_result["parameters"]

    intent_name = query_result["intent"]["displayName"]

    if intent_name == "payment.initiate-payment":
        return create_payment_request(parameters)

    elif intent_name == "account.balance_check":
        return get_account_balance(parameters)


def create_payment_request(parameters):
    temp_dialogflow_response = DIALOGFLOW_RESPONSE_TEMPLATE
    response_message = "Thanks for submitting your payment request, we'll let you know once the request is processed"

    try:

        PaymentRequest.objects.create(
            sender_name=parameters["name-of-receiver"],
            request_initiated_type="DialogFlow",
            receiver_name=parameters["name-of-receiver"],
            amount=parameters["amount"],
        )
    except:
        logger.exception(
            "The below error occurred while creating a new payment request object."
        )
        # TODO: this needs a better message response
        response_message = "There was an error while creating your payment request. Please try again later"

    temp_dialogflow_response["fulfillmentMessages"][0]["text"]["text"] = [
        response_message
    ]

    return JsonResponse(temp_dialogflow_response)


def get_account_balance(parameters):
    temp_dialogflow_response = DIALOGFLOW_RESPONSE_TEMPLATE

    try:

        account_number = parameters["account-number"]

        logger.info(f"Trying to retrieve balance for account number - {account_number}")

        account_obj: BankAccount = BankAccount.objects.filter(
            account_number=account_number
        ).first()

        response_message = f"Your account balance is {account_obj.amount}"

        temp_dialogflow_response["fulfillmentMessages"][0]["text"]["text"] = [
            response_message
        ]

        logger.info("Successfully retrieved the balance.")

    except:
        logger.exception(
            "The below error occurred while retreiving the balance for the customer"
        )
        response_message = "There was an error while retreving your account balance. Please try again later"

    temp_dialogflow_response["fulfillmentMessages"][0]["text"]["text"] = [
        response_message
    ]

    return JsonResponse(temp_dialogflow_response)
