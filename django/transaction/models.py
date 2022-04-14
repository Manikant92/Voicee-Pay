from django.db import models
from transaction.constants import (
    ACCOUNT_STATUS_CHOICES,
    PAYMENT_REQUEST_STATUS_CHOICES,
    REQUEST_INITIATED_TYPE_CHOICES,
    TRANSACTION_STATUS_CHOICES,
)


class PaymentRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request_initiated_type = models.CharField(
        choices=REQUEST_INITIATED_TYPE_CHOICES, max_length=20
    )
    receiver_name = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=50)
    status = models.CharField(choices=PAYMENT_REQUEST_STATUS_CHOICES, max_length=40, default="pending")


class BankAccount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    account_number = models.CharField(max_length=18, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=30)

    def __str__(self) -> str:
        return f"{self.account_number}"


class Bank(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True, help_text="Name of the bank")
    address = models.TextField(null=True, blank=True, help_text="Address of the bank")

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

    bank_name = models.ForeignKey(Bank, to_field="name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class BankBranch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, unique=True)
    ifse_code = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)

    bank_name = models.ForeignKey(Bank, to_field="name", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=50)
    receiver_name = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=50)
    bank_name = models.ForeignKey(Bank, to_field="name", on_delete=models.CASCADE)
    branch_name = models.ForeignKey(
        BankBranch, to_field="name", on_delete=models.CASCADE
    )
    account_number = models.ForeignKey(
        BankAccount, to_field="account_number", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    status = models.CharField(choices=TRANSACTION_STATUS_CHOICES, max_length=40, default="pending")

    def __str__(self) -> str:
        return f"{self.transaction_id}"
