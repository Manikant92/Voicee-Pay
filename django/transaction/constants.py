REQUEST_INITIATED_TYPE_CHOICES = (
    ("Manual", "Manual"),
    ("DialogFlow", "DialogFlow"),
)

ACCOUNT_STATUS_CHOICES = (("Active", "Active"), ("Deactivated", "Deactivated"))

TRANSACTION_STATUS_CHOICES = (
    (
        "Successful",
        "Successful",
    ),
    ("Failed", "Failed"),
    ("Insufficient Fund", "Insufficient Fund"),
    ("pending", "pending"),
)


PAYMENT_REQUEST_STATUS_CHOICES = (
    ("Acted upon", "Acted upon"),
    ("pending", "pending"),
    ("Failed", "Failed"),
)
