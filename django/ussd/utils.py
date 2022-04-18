from decimal import Decimal
import logging
from typing import Callable
from .constants import CODE_FUNCTION_MAPPING, LANGUAGE_CODE_MAPPING, USSD_RESPONSES
from transaction.models import Customer, Transaction, generate_numbers

logger = logging.getLogger("django")


def display_services(user_input: str, customer_obj: Customer, language_code: str):
    response = USSD_RESPONSES.get(language_code).get("initial")
    logger.info(f"Language Code - {language_code}")
    return response, language_code


def check_balance_with_phone_number(
    user_input: str, customer_obj: Customer, language_code: str
):
    logger.info(f"Trying to fetch balance for customer - {customer_obj.name}")
    response = ""

    if customer_obj:
        response = USSD_RESPONSES.get(language_code).get("balance_response") + str(
            customer_obj.account_number.amount
        )
    else:
        logger.info(f"No account found for customer - {customer_obj.name}")

    return response, language_code


def transfer_money(user_input: str, sender: Customer, language_code: str = "en"):

    # get the language code from string
    language_code_str = LANGUAGE_CODE_MAPPING.get(language_code)
    user_input = user_input.replace(f"{language_code_str}*2*", "")

    account_number, amount_to_send = user_input.split(",")
    amount_to_send = Decimal(amount_to_send)
    response = ""
    try:
        recepient: Customer = Customer.objects.filter(
            account_number=account_number
        ).first()

        sender_balance = sender.account_number.amount

        if sender and recepient and sender_balance >= amount_to_send:

            Transaction.objects.create(
                transaction_id=generate_numbers(15),
                sender_account=sender,
                receiver_account=recepient,
                amount=amount_to_send,
            )
            logger.info("transaction created successfull!")

            # add money to the reepient
            recepient.account_number.amount += amount_to_send
            recepient.account_number.save()

            # deduct money from the sender
            sender.account_number.amount -= amount_to_send
            sender.account_number.save()

            amount_to_send = str(amount_to_send)

            logger.info(
                f"language - {language_code} - Transfering Rs.{amount_to_send} from {sender.name} to {recepient.name}"
            )

            # response = f"END Successfully transferred Rs.{amount_to_send} to {recepient.name}"
            response = USSD_RESPONSES.get(language_code).get("transfer_success")
            response = response.replace("amount_to_send", amount_to_send).replace(
                "recepient.name", recepient.name
            )

        else:
            # response = f"END Failed to transfer Rs.{amount_to_send} to {recepient.name}"
            response = USSD_RESPONSES.get(language_code).get("transfer_failed")
            response = response.replace("amount_to_send", amount_to_send).replace(
                "recepient.name", recepient.name
            )

            if sender_balance < amount_to_send:
                # response = f"END Insufficient fund to transfer Rs.{amount_to_send} to {recepient.name}. \nYou need Rs.{amount_to_send - sender_balance} more to make this transaction."
                response = USSD_RESPONSES.get(language_code).get(
                    "unsufficient_fund_error"
                )
                response = response.replace("amount_to_send", amount_to_send).replace(
                    "insufficient_fund", str(amount_to_send - sender_balance)
                )

    except:
        logger.exception("There was an exception while transfering the amount")
        # response = f"END Failed to transfer Rs.{amount_to_send} to {recepient.name}"
        response = USSD_RESPONSES.get(language_code).get("transfer_failed")
        response = response.replace("amount_to_send", amount_to_send).replace(
            "recepient.name", recepient.name
        )

    return response, language_code


def transfer_money_prompt(user_input: str, customer_obj: Customer, language_code: str):
    return USSD_RESPONSES.get(language_code).get("transfer_money_prompt"), language_code


def ussd_connection_terminate(
    user_input: str, customer_obj: Customer, language_code: str
):
    return USSD_RESPONSES[language_code]["ussd_connection_terminate"], language_code


# TODO: might need something mode simple
def get_matched_code(user_input: str, code: str):

    return True if user_input.startswith(code) else False


def execute_action(user_input: str, customer_obj: Customer):

    language_code = ""
    response = ""
    # initial trigger from USSD service
    if user_input == "":
        if customer_obj:
            response = USSD_RESPONSES.get("select_language")
        else:
            logger.info("Customer doesn't have an account yet.")
            response = USSD_RESPONSES.get("no_account_error")

    else:
        logger.info(f"Customer - {customer_obj.name}")
        for code, content in CODE_FUNCTION_MAPPING.items():
            if get_matched_code(user_input, code):

                method_name = content.get("method_name", False)

                # get the callable method from the current file
                callable_action_method: Callable = globals()[method_name]
                logger.info(f"Executing - {callable_action_method.__name__}")

                response, language_code = callable_action_method(
                    user_input, customer_obj, *content["args"]
                )
                break

    if response == "":
        response = USSD_RESPONSES.get(language_code).get("default_error")

    return response
