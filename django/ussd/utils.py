import logging
from transaction.models import Customer

logger = logging.getLogger("django")


def check_balance_with_phone_number(phone_number):
    logger.info(f"Trying to fetch balance for phone number - {phone_number}")
    customer_obj: Customer = Customer.objects.filter(phone_number=phone_number).first()

    if customer_obj:

        return str(customer_obj.account_number.amount)
    else:
        logger.info(f"No account found for phone number - {phone_number}")
        return "0"
