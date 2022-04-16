from django.http import HttpResponse
import logging

logger = logging.getLogger("django")


def af_webhook(request):
    if request.method == "POST":
        logger.info("Triggered Africa Talking Webhook!")
        response = "END Response successful! \n need"
        try:

            session_id = request.POST["sessionId"]
        # user = g.current_user
        # session = g.session
        # user_response = g.user_response
        # if isinstance(user, AnonymousUser):
        #     # register user
        #     menu = RegistrationMenu(session_id=session_id, session=session, phone_number=g.phone_number,
        #                             user_response=user_response, user=user)
        #     return menu.execute()
        # level = session.get('level')
        # if level < 2:
        #     menu = LowerLevelMenu(session_id=session_id, session=session, phone_number=g.phone_number,
        #                         user_response=user_response, user=user)
        #     return menu.execute()

        # if level >= 50:
        #     menu = Deposit(session_id=session_id, session=session, phone_number=g.phone_number,
        #                 user_response=user_response, user=user, level=level)
        #     return menu.execute()

        # if level >= 40:
        #     menu = WithDrawal(session_id=session_id, session=session, phone_number=g.phone_number,
        #                     user_response=user_response, user=user, level=level)
        #     return menu.execute()

        # if level >= 10:
        #     menu = Airtime(session_id=session_id, session=session, phone_number=g.phone_number, user_response=user_response,
        #                 user=user, level=level)
        #     return menu.execute()

        # response = make_response("END nothing here", 200)
        # response.headers['Content-Type'] = "text/plain"
        except:
            logger.exception("There is an error while responding!")

        logger.info("sending response")
        
        return HttpResponse(response, content_type="text/plain")

    else:
        return HttpResponse(
            "This is the Africa Talking webhook URL. Send a post request"
        )
