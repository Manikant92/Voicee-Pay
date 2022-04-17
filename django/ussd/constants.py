from collections import OrderedDict

USSD_RESPONSES = {
    "select_language": """CON 1. தமிழ்
    2.മലയാളം
    3.ಕನ್ನಡ
    4.हिंदी
    5.मराठी
    6.English""",
    "hi": {
        "initial": """CON 1.बैंक बैलेंस चेक करें
        2.धन हस्तांतरण
        3.बाहर निकलना""",
        "balance_response": "END संतुलन : Rs.",
        "ussd_connection_terminate": "END हमारे साथ बैंकिंग के लिए धन्यवाद.\nआपका दिन शुभ हो!\n - सिटी बैंक",
        "transfer_money": "CON अल्पविराम से अलग खाता संख्या और राशि दर्ज करें ','",
        "transfer_success": "END Your transfer was successful",
        "transfer_failed": "END Your transfer failed!",
        "no_account_error": "END You don't have an account yet.",
        "unsufficient_fund_error": "END You don't have a sufficient fund to make this tranfer.",
    },
    "en": {
        "initial": """CON Welcome to Citi Bank
        1.Check Bank balance
        2.Transfer Money
        3.Exit""",
        "balance_response": "END Balance : Rs.",
        "ussd_connection_terminate": "END Thanks for banking with us.\nHave a great day!\n - Citi bank",
        "transfer_money_prompt": "CON Enter the account number and amount seperated with comma ','",
        "transfer_success": "END Successfully transferred Rs.amount_to_send to recepient.name",
        "transfer_failed": "END Failed to transfer Rs.<amount_to_send> to <recepient.name>!",
        "no_account_error": "END You don't have an account yet.",
        "unsufficient_fund_error": "END Insufficient fund to transfer Rs.amount_to_send to recepient.name. \nYou need Rs.unsufficient_fund more to make this transaction.",
        "default_error": "END We can't process request now.",
    },
    "no_account_error": "END You don't have an account yet.",
}

LANGUAGE_CODE_MAPPING = {
    "ta": "1",
    "mal": "2",
    "ka": "3",
    "hi": "4",
    "mar": "5",
    "en": "6",
}

CODE_FUNCTION_MAPPING = OrderedDict(
    {
        "6*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["en"],
        },
        "6*2*": {
            "method_name": "transfer_money",
            "args": ["en"],
        },
        "6*2": {
            "method_name": "transfer_money_prompt",
            "args": ["en"],
        },
        "6*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["en"],
        },
        "6": {
            "method_name": "display_services",
            "args": ["en"],
        },
        "5*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["hi"],
        },
        "5*2": {
            "method_name": "transfer_money",
            "args": ["hi"],
        },
        "5*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["hi"],
        },
        "5": {
            "method_name": "display_services",
            "args": ["hi"],
        },
        "4*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["hi"],
        },
        "4*2": {
            "method_name": "transfer_money",
            "args": ["hi"],
        },
        "4*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["hi"],
        },
        "4": {
            "method_name": "display_services",
            "args": ["hi"],
        },
        "3*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["ta"],
        },
        "3*2": {
            "method_name": "transfer_money",
            "args": ["ta"],
        },
        "3*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["hi"],
        },
        "3": {
            "method_name": "display_services",
            "args": ["ta"],
        },
        "2*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["mal"],
        },
        "2*2": {
            "method_name": "transfer_money",
            "args": ["mal"],
        },
        "2*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["mal"],
        },
        "2": {
            "method_name": "display_services",
            "args": ["mal"],
        },
        "1*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["ta"],
        },
        "1*2": {
            "method_name": "transfer_money",
            "args": ["ta"],
        },
        "1": {
            "method_name": "display_services",
            "args": ["ta"],
        },
        "": {"": "langauge_select"},
    }
)
