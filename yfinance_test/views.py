from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import (
    api_view,
    throttle_classes,
)
from django.http import JsonResponse
import yfinance as yf

from core.utils import exception_handler, LOGGER


@api_view(["GET"])
@throttle_classes([UserRateThrottle])
@exception_handler
def get_daily_price(request, ticker, from_date, to_date):
    """ Return a timeseries with the price info of the company associated with
        a ticker for the specified start_date and end_date dates
    Args:
        request (request): django request object, has user object among
            other attributes
        ticker (string): short name for a company
        from_date (string): starting date to get the information from in the
            format yyyy-mm-dd
        to_date (string): (optional) end date to get the information from in
            the format yyyy-mm-dd, if not value is set, current date is used

    Returns:
        JsonResponse (object): Returns timeseries of the associated company
    """
    LOGGER.debug("Getting the daily price timeseries")
    # get the information
    data = yf.download(ticker, start=from_date, end=to_date)

    # different ways to convert the data
    # from collections import OrderedDict
    # return_data = data.to_dict(into=OrderedDict)
    # data.index = data.index.map(str)

    # format the timestamp data from the index
    data.index = data.index.strftime("%Y-%m-%d")
    # convert to dictionary
    return_data = data.to_dict()

    # return a json string
    # return_data = data.to_json()

    # i kept the adj close value, not sure if it's necessary
    return JsonResponse(return_data, safe=False)
