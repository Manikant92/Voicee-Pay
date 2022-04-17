import logging
from transaction.models import Customer, Transaction, generate_numbers

logger = logging.getLogger("django")


def check_balance_with_phone_number(phone_number):
    logger.info(f"Trying to fetch balance for phone number - {phone_number}")
    customer_obj: Customer = Customer.objects.filter(phone_number=phone_number).first()
    response = ""

    if customer_obj:
        response = str(customer_obj.account_number.amount)
    else:
        logger.info(f"No account found for phone number - {phone_number}")
        response = "0"

    return response


def transfer_money(user_input: str, phone_number: str):

    account_number, amount_to_send = user_input.split(",")
    response = ""

    try:
        sender: Customer = Customer.objects.filter(phone_number=phone_number).first()

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

            recepient.account_number.amount += amount_to_send
            recepient.account_number.save()

            logger.info(
                f"Transfering Rs.{amount_to_send} from {sender.name} to {recepient.name}"
            )

            response = f"END Successfully transfered Rs.{amount_to_send} to {recepient.name}"

        else:
            response = f"END Failed to transfer Rs.{amount_to_send} to {recepient.name}"
            if sender_balance < amount_to_send:
                response = f"END Insufficient fund to transfer Rs.{amount_to_send} to {recepient.name}. \nYou need Rs.{amount_to_send - sender_balance} more to make this transaction."
    except:
        logger.exception("There was an exception while transfering the amount")
        response = f"END Failed to transfer Rs.{amount_to_send} to {recepient.name}"

    return response
