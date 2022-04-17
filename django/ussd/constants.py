USSD_RESPONSES = {
    "initial": """CON 1.Check Bank balance
2.Transfer Money
3.Exit""",
    "balance_response": "END Balance : Rs.",
    "end": "END Thanks for banking with us.\nHave a great day!\n - Citi bank",
    "transfer_money": "CON Enter the account number and amount seperated with comma ','",
    "transfer_success": "END Your transfer was successful",
    "transfer_failed": "END Your transfer failed!",
    "no_account_error": "END You don't have an account yet.",
    "unsufficient_fund_error": "END You don't have a sufficient fund to make this tranfer."
}
