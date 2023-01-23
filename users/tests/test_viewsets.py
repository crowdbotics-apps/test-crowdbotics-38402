import uuid

import pytest
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate

from users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestUserViewSet:
    client = APIClient()

    def test_should_return_401_if_no_token_provided(self):
        url = "/api/v1/user/user/subscriptions/"
        response = self.client.get(url)
        assert response.status_code == HTTP_401_UNAUTHORIZED

    @pytest.mark.django_db
    def test_should_return_200_and_list_user_resources(self):
        user = UserFactory()
        url = f"/api/v1/user/user/subscriptions/"
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = self.client.get(url)
        assert request.status_code == HTTP_200_OK