from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from home.api.v1.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)