from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.models import Applications
from subscriptions.models import Subscription
from .serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token

from .utils import check_subscription_plan


class ApplicationViewSet(viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Applications.objects.all()

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        request_token = Token.objects.filter(key=request.auth).first()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subscription = Subscription.objects.get(user=request_token.user)
        app_data, status_code = check_subscription_plan(subscription, request)
        return Response(data=app_data, status=status_code)

    def list(self, request, *args, **kwargs):
        self.serializer_class(self.queryset, many=True)
        return Response(self.serializer_class.data)
