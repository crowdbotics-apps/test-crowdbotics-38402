import uuid

import pytest
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.test import APIClient

from users.tests.factories import UserFactory
from rest_framework.authtoken.models import Token


pytestmark = pytest.mark.django_db


class TestUserViewSet:
    client = APIClient()

    def test_should_return_401_if_no_token_provided(self):
        url = "/api/v1/user/subscriptions/"
        response = self.client.get(url)
        assert response.status_code == HTTP_401_UNAUTHORIZED
