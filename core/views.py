from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import (
    api_view,
    throttle_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from core.utils import LOGGER


@api_view(["GET"])
@throttle_classes([UserRateThrottle])
@permission_classes([~IsAuthenticated])
def health_check(request):
    """ Checks if the server is running
    Args:
        request (request): django request object, has user object

    Returns:
        HttpResponse: Returns empty string and 200 status
    """
    LOGGER.debug("I'm alive!")
    return HttpResponse("")