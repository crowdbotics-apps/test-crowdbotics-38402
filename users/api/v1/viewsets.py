from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from home.api.v1.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(student)
        return Response(serializer.data)
