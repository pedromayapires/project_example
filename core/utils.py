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
        # for frontend display
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
            # More should be done here, like send an email do admin users
            # ************************************************************
            return JsonResponse(
                {
                    # 0 an unexpected, more serious, exception
                    "error_level": 0,
                    "message": "Unexpected error, admins will be notified",
                }
            )

    return wrapper_function
