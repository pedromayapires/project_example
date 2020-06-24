from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r"^get_daily_price/(?P<ticker>\w+)/"
        + "(?P<from_date>[0-9]{4}-[0-9]{2}-[0-9]{2})"
        + "(/(?P<to_date>[0-9]{4}-[0-9]{2}-[0-9]{2}))?$",
        views.get_daily_price,
    ),
]
