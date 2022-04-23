from collections import OrderedDict

USSD_RESPONSES = {
    "select_language": """CON 1. தமிழ்
    2.മലയാളം
    3.ಕನ್ನಡ
    4.हिंदी
    5.বাংলা
    6.English
    7.తెలుగు""",
    "mal": {
        "initial": """CON സിറ്റി ബാങ്കിലേക്ക് സ്വാഗതം
        1.ബാങ്ക് ബാലൻസ് പരിശോധിക്കുക
        2.പണം കൈമാറുക / പണം അയക്കുക
        3.പുറത്തേക്""",
        "balance_response": "END ബാലൻസ് : Rs.",
        "ussd_connection_terminate": "END ഞങ്ങളോടൊപ്പം ബാങ്കിംഗ് നടത്തിയതിന് നന്ദി.\n ശുഭദിനാശംസകൾ!\n - സിറ്റി ബാങ്ക്",
        "transfer_money_prompt": "CON അക്കൗണ്ട് നമ്പറും തുകയും കോമ ഉപയോഗിച്ച് വേർതിരിച്ചു നൽകുക','",
        "transfer_success": "END recipient.name-ലേക്ക് Rs.amount_to_send വിജയകരമായി അയച്ചിരിക്കുന്നു.",
        "transfer_failed": "END recipient.name എന്നതിലേക്ക് Rs.amount_to_send കൈമാറുന്നതിൽ പരാജയപ്പെട്ടു!",
        "no_account_error": "END താങ്കളുടെ പേരിൽ ഒരു അക്കൗണ്ട് നിലവിൽ  ഇല്ല.",
        "insufficient_fund_error": "END recipient.name-ലേക്ക് Rs.amount_to_send ട്രാൻസ്ഫർ ചെയ്യാൻ ഫണ്ട് അപര്യാപ്തമാണ്. \nഈ ഇടപാട് നടത്താൻ നിങ്ങൾക്ക് Rs.insufficient_fund കൂടുതൽ ആവശ്യമാണ്.",
        "default_error": "END ഇപ്പോൾ ഈ അഭ്യർത്ഥന തുടരുവാൻ സാധിക്കുകയില്ല.",
    },
    "hi": {
        "initial": """CON टी बैंक में आपका स्वागत है
        1.शेष राशि पूछताछ
        2.धन हस्तांतरण
        3.बाहर निकलना""",
        "balance_response": "END संतुलन : Rs.",
        "ussd_connection_terminate": "END हमारे साथ बैंकिंग के लिए धन्यवाद.\nआपका दिन शुभ हो!\n - सिटी बैंक",
        "transfer_money_prompt": "CON अल्पविराम से अलग खाता संख्या और राशि दर्ज करें ','",
        "transfer_success": "END  recipient.name को ₹. amount_to_send अंतरण करने में सफ़ल",
        "transfer_failed": "END recipient.name को ₹.<amount_to_send> अंतरण करने में असफल",
        "no_account_error": "END   आपके पास अभितक खाता नहीं है.",
        "insufficient_fund_error": "END recipient.name को  ₹.amount_to_send अंतरण करने के लिए अपर्याप्त निधि",
        "default_error": "END हम अभी अनुरोधों को संसाधित नहीं कर सकते.",
    },
    "en": {
        "initial": """CON Welcome to Citi Bank
        1.Check Bank balance
        2.Transfer Money
        3.Exit""",
        "balance_response": "END Balance : Rs.",
        "ussd_connection_terminate": "END Thanks for banking with us.\nHave a great day!\n - Citi bank",
        "transfer_money_prompt": "CON Enter the account number and amount seperated with comma ','",
        "transfer_success": "END Successfully transferred Rs.amount_to_send to recipient.name",
        "transfer_failed": "END Failed to transfer Rs.amount_to_send to recipient.name!",
        "no_account_error": "END You don't have an account yet.",
        "insufficient_fund_error": "END Insufficient fund to transfer Rs.amount_to_send to recipient.name. \nYou need Rs.insufficient_fund more to make this transaction.",
        "default_error": "END We can't process request now.",
    },
    "ben": {
        "initial": """CON সিটি ব্যাংকে স্বাগতম
        1.ব্যাঙ্ক ব্যালেন্স চেক করুন
        2.অর্থ স্থানান্তর করুন
        3.প্রস্থান করুন/প্রস্থান""",
        "balance_response": "END ব্যালেন্স : Rs.",
        "ussd_connection_terminate": "END আমাদের সাথে ব্যাংকিং করার জন্য ধন্যবাদ| আপনার দিন শুভ হোক! \n- সিটি ব্যাংক",
        "transfer_money_prompt": "CON কমা দিয়ে(',') আলাদা করে অ্যাকাউন্ট নম্বর এবং অর্থের পরিমাণ লিখুন। ",
        "transfer_success": "END সফলভাবে Rs.amount_to_send recipient.name -এ স্থানান্তর করা হয়েছে।",
        "transfer_failed": "END recipient.name -এ Rs.amount_to_send স্থানান্তর করতে ব্যর্থ হয়েছে!!",
        "no_account_error": "ENDআপনার এখনও একটি অ্যাকাউন্ট নেই.",
        "insufficient_fund_error": "END recipient.name -এ Rs.amount_to_send স্থানান্তর করার জন্য অপর্যাপ্ত অর্থ রয়েছে।. \nএই লেনদেন করার জন্য আপনার আরও Rs.insufficient_fund প্রয়োজন৷.",
        "default_error": "END আমরা এখন অনুরোধটি প্রসেস করতে পারছি না|.",
    },
    "no_account_error": "END You don't have an account yet.",
}

LANGUAGE_CODE_MAPPING = {
    "ta": "1",
    "mal": "2",
    "ka": "3",
    "hi": "4",
    "ben": "5",
    "en": "6",
    "te": "7",
}

# OrderDict is to make sure we match with the right options
CODE_FUNCTION_MAPPING = OrderedDict(
    {
        "7*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["te"],
        },
        "7*2*": {
            "method_name": "transfer_money",
            "args": ["te"],
        },
        "7*2": {
            "method_name": "transfer_money_prompt",
            "args": ["te"],
        },
        "7*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["te"],
        },
        "7": {
            "method_name": "display_services",
            "args": ["te"],
        },
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
            "args": ["ben"],
        },
        "5*2*": {
            "method_name": "transfer_money",
            "args": ["ben"],
        },
        "5*2": {
            "method_name": "transfer_money_prompt",
            "args": ["ben"],
        },
        "5*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["ben"],
        },
        "5": {
            "method_name": "display_services",
            "args": ["ben"],
        },
        "4*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["hi"],
        },
        "4*2*": {
            "method_name": "transfer_money",
            "args": ["hi"],
        },
        "4*2": {
            "method_name": "transfer_money_prompt",
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
            "args": ["ka"],
        },
        "3*2*": {
            "method_name": "transfer_money",
            "args": ["ka"],
        },
        "3*2": {
            "method_name": "transfer_money_prompt",
            "args": ["ka"],
        },
        "3*1": {
            "method_name": "check_balance_with_phone_number",
            "args": ["ka"],
        },
        "3": {
            "method_name": "display_services",
            "args": ["ka"],
        },
        "2*3": {
            "method_name": "ussd_connection_terminate",
            "args": ["mal"],
        },
        "2*2*": {
            "method_name": "transfer_money",
            "args": ["mal"],
        },
        "2*2": {
            "method_name": "transfer_money_prompt",
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
        "1*2*": {
            "method_name": "transfer_money",
            "args": ["ta"],
        },
        "1*2": {
            "method_name": "transfer_money_prompt",
            "args": ["ta"],
        },
        "1": {
            "method_name": "display_services",
            "args": ["ta"],
        },
        "": {"": "langauge_select"},
    }
)
