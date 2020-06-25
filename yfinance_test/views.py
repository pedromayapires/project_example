# from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import (
    api_view,
    # throttle_classes,
)
from django.http import JsonResponse
from datetime import datetime
import yfinance as yf

from core.utils import exception_handler, LOGGER

# yfinance github page
# https://github.com/ranaroussi/yfinance


@api_view(["GET"])
# @throttle_classes([UserRateThrottle])
@exception_handler
def get_daily_price(request, ticker, from_date, to_date=None):
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

    # if to_date is not set, this will default it to the current day
    if not to_date:
        to_date = datetime.today().strftime("%Y-%m-%d")

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
    # can remove the extra data
    return JsonResponse(return_data, safe=False)


@api_view(["GET"])
# @throttle_classes([UserRateThrottle])
@exception_handler
def get_company_info(request, ticker):
    """ Get company info (sector, address, symbol/ticker, short name)
    Args:
        request (request): django request object, has user object among
            other attributes
        ticker (string): short name for a company

    Returns:
        JsonResponse (object): Returns the company information
    """
    LOGGER.debug("Get company info")
    # get the information
    ticker = yf.Ticker(ticker)
    return_data = ticker.info

    # i kept all data regarding the company, not sure if it's necessary
    # can remove the extra data
    return JsonResponse(return_data, safe=False)


@api_view(["GET"])
# @throttle_classes([UserRateThrottle])
@exception_handler
def get_recommendations(request, ticker, from_date, to_date=None):
    """ Return a timeseries with average daily sentiment for the company
        associated with a ticker for the specified start_date and end_date
    Args:
        request (request): django request object, has user object among
            other attributes
        ticker (string): short name for a company
        from_date (string): starting date to get the information from in the
            format yyyy-mm-dd
        to_date (string): (optional) end date to get the information from in
            the format yyyy-mm-dd, if not value is set, current date is used

    Returns:
        JsonResponse (object): Returns the company recommendations data
    """
    LOGGER.debug("Get the company recommendations data")

    # if to_date is not set, this will default it to the current day
    if not to_date:
        to_date = datetime.today().strftime("%Y-%m-%d")

    # get the recommendations data
    ticker = yf.Ticker(ticker)

    # this doesn't return what we want
    # hist = ticker.history(start=from_date, end=to_date)

    # From Grade and To Grade fields are the only ones that matter?
    # is the idea to filter the dates obtained or is there a way to filter the
    # data from the library itself?
    data = ticker.recommendations

    # does not work
    # return_data = data[data.index.between(from_date, to_date)]

    import datetime
    from datetime import date

    # df.loc[(df.date >= i[0]) & (df.date <= i[-1])]
    # .loc['2000-6-1':'2000-6-10']
    # returned_data = data.index.to_datetime()
    # data.loc(
    #     (data.index >= date.fromisoformat(from_date))
    #     & (data.index <= date.fromisoformat(to_date))
    # )
    return_data = data["From Grade"].loc[from_date:to_date]
    # LOGGER.debug(data)
    # LOGGER.debug("----------------------------")
    LOGGER.debug(return_data)
    LOGGER.debug("----------------------------")
    LOGGER.debug(data["From Grade"][return_data])

    # convert the timestamp info
    data.index = data.index.strftime("%Y-%m-%d")
    # get the data in dictionary format
    return_data = data.to_dict()

    return JsonResponse(return_data, safe=False)
