import pytest
from users.tests.factories import UserFactory
from rest_framework.authtoken.models import Token


def mock_client(self, url):
    user = UserFactory()
    token = Token.objects.create(user=user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    request = self.client.get(url)
    return request