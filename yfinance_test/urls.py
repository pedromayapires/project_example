from django.conf.urls import url
from . import views

urlpatterns = [
    # server/yfinance_test/get_daily_price/msft/2020-01-01/2020-06-01
    url(
        r"^get_daily_price/(?P<ticker>\w+)/"
        + "(?P<from_date>[0-9]{4}-[0-9]{2}-[0-9]{2})"
        + "(/(?P<to_date>[0-9]{4}-[0-9]{2}-[0-9]{2}))?$",
        views.get_daily_price,
    ),
    # server/yfinance_test/get_company_info/msft
    url(r"^get_company_info/(?P<ticker>\w+)$", views.get_company_info),
    # server/yfinance_test/get_recommendations/msft/2020-01-01/2020-06-01
    url(
        r"^get_recommendations/(?P<ticker>\w+)/"
        + "(?P<from_date>[0-9]{4}-[0-9]{2}-[0-9]{2})"
        + "(/(?P<to_date>[0-9]{4}-[0-9]{2}-[0-9]{2}))?$",
        views.get_recommendations,
    ),
]
