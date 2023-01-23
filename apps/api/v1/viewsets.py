from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.models import Applications
from subscriptions.models import Subscription
from .serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .utils import check_subscription_plan


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Applications.objects.all()