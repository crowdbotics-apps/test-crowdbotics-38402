from rest_framework import authentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response


class SubscriptionPaymentViewSet(viewsets.ViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()


class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()

    def retrieve(self, request, pk=None):
        subscription = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(subscription)
        return Response(serializer.data)

    def list(self, request):
        if not self.queryset:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        subscription_id = kwargs.get("pk", None)

        if not subscription_id:
            return Response(status=HTTP_404_NOT_FOUND)

        subscription = Subscription.objects.filter(id=subscription_id, active=True).first()

        if not subscription:
            return Response(status=HTTP_404_NOT_FOUND)

        subscription.active = False
        subscription.save()

        return Response(status=HTTP_204_NO_CONTENT)
