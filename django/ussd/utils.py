import logging
from transaction.models import Customer, Transaction, generate_numbers

logger = logging.getLogger("django")


def check_balance_with_phone_number(phone_number):
    logger.info(f"Trying to fetch balance for phone number - {phone_number}")
    customer_obj: Customer = Customer.objects.filter(phone_number=phone_number).first()

    if customer_obj:
        return str(customer_obj.account_number.amount)
    else:
        logger.info(f"No account found for phone number - {phone_number}")
        return "0"


def transfer_money(user_input: str, phone_number: str):

    account_number, amount = user_input.split(",")
    response = ""

    try:
        sender: Customer = Customer.objects.filter(phone_number=phone_number).first()

        recepient: Customer = Customer.objects.filter(
            account_number=account_number
        ).first()

        if sender and recepient and sender.account_number.amount >= amount:

            Transaction.objects.create(
                transaction_id=generate_numbers(15),
                sender_account=sender,
                receiver_account=recepient,
                amount=amount,
            )
            logger.info("transaction created successfull!")

            recepient.account_number.amount += amount
            recepient.account_number.save()

            logger.info(
                f"Transfering Rs.{amount} from {sender.name} to {recepient.name}"
            )

            response = f"END Successfully transfered Rs.{amount} to {recepient.name}"

        else:
            response = f"END Failed to transfer Rs.{amount} to {recepient.name}"
    except:
        logger.exception("There was an exception while transfering the amount")
        response = f"END Failed to transfer Rs.{amount} to {recepient.name}"

    return response
