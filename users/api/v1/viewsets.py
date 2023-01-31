from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from home.api.v1.serializers import UserSerializer
from plans.models import Plan
from subscriptions.models import Subscription
from users.models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request):
        plan = Plan.objects.filter(name="FREE").first()
        if not plan:
            Subscription.objects.create(user=request.user, plan=plan)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def retrieve(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        if not Subscription.objects.filter(user=user).first():
            Subscription.objects.create(user=user, plan=Plan.objects.filter(name="FREE").first())
            return Response(status=HTTP_200_OK, data={"data": f"User has been associated with a Subscription"})
        return Response(status=HTTP_200_OK, data={"data": f"User already has a subscription"})
