from django.http import JsonResponse
from django.conf import settings

import logging

LOGGER = logging.getLogger()
logging.config.dictConfig(settings.LOGGER_CONFIG)


def exception_handler(function):
    def wrapper_function(*args, **kwargs):
        try:
            # run original function
            return function(*args, **kwargs)
        # catch other types of exceptions and handle them with different levels
        # for frontend display, maybe just send httpresponse with appropriate
        # status
        # except OtherException as ex:
        #     LOGGER.exception(str(ex))
        #     return JsonResponse(
        #         {
        #             # Corresponding level
        #             "error_level": 0,
        #             # Warning or something else
        #             "message": "",
        #         }
        #     )
        except Exception as ex:
            # this will be logged in a file
            LOGGER.exception(str(ex))
            # ************************************************************
            # More could be done here, like send an email do admin users
            # ************************************************************
            return JsonResponse({"message": "Logged unexpected error"})

    return wrapper_function
