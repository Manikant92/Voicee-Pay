from django.db import models
from django.db.models.signals import pre_save
from string import digits
import random
from transaction.constants import (
    ACCOUNT_STATUS_CHOICES,
    PAYMENT_REQUEST_STATUS_CHOICES,
    REQUEST_INITIATED_TYPE_CHOICES,
    TRANSACTION_STATUS_CHOICES,
)


def generate_numbers(size=4):
    return "".join(random.choice(digits) for _ in range(size))


def generate_account_number():
    return f"1{generate_numbers()[1:]}-" + "-".join(
        [generate_numbers() for _ in range(3)]
    )


class PaymentRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request_initiated_type = models.CharField(
        choices=REQUEST_INITIATED_TYPE_CHOICES, max_length=20
    )
    receiver_name = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=50)
    status = models.CharField(
        choices=PAYMENT_REQUEST_STATUS_CHOICES, max_length=40, default="pending"
    )
    amount = models.DecimalField(decimal_places=2, max_digits=30, default=0.0)


class BankAccount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    account_number = models.CharField(
        max_length=19, unique=True, default=generate_account_number()
    )
    amount = models.DecimalField(decimal_places=2, max_digits=30, default=0.0)

    def __str__(self) -> str:
        return f"{self.account_number}"


class BankBranch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    ifse_code = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    is_active = models.CharField(choices=ACCOUNT_STATUS_CHOICES, max_length=15)
    last_modified = models.DateTimeField(auto_now=True)

    account_number = models.ForeignKey(
        BankAccount, to_field="account_number", on_delete=models.CASCADE
    )

    branch_name = models.ForeignKey(
        BankBranch, to_field="name", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=50)

    sender_account = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="sender_account",
        default="",
    )
    receiver_account = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="receiver_account",
        default="",
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    status = models.CharField(
        choices=TRANSACTION_STATUS_CHOICES, max_length=40, default="pending"
    )

    def __str__(self) -> str:
        return f"{self.transaction_id}"


# generate new account number and override the default
def pre_save_create_account_number(sender, instance, *args, **kwargs):
    if not instance.account_number:
        instance.account_number = generate_account_number()


pre_save.connect(pre_save_create_account_number, sender=BankAccount)
