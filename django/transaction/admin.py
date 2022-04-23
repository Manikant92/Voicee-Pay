from django.contrib import admin

from .models import (
    Customer,
    BankAccount,
    Feedback,
    PaymentRequest,
    BankBranch,
    Transaction,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "is_active", "account_number")


@admin.register(PaymentRequest)
class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "receiver_name",
        "sender_name",
        "status",
        "request_initiated_type",
    )


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("account_number", "amount", "created_at")


@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ("name", "ifse_code")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "transaction_id",
        "sender_account",
        "receiver_account",
        "amount",
        "status",
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("created_at", "feedback")
