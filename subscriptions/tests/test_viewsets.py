import pytest
import json
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from subscriptions.models import Subscription
from users.tests.factories import UserFactory


@pytest.mark.django_db
class TestSubscriptionViews:
    client = APIClient()
    url = "/api/v1/subscriptions/"

    def test_should_return_401_if_no_token_provided(self):
        response = self.client.get(self.url)
        assert response.status_code == HTTP_401_UNAUTHORIZED

    def test_should_return_404_if_subscription_not_found(self):
        user = UserFactory()
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(self.url)
        assert response.status_code == HTTP_404_NOT_FOUND

    def test_should_return_200_if_subscription_founded(self):
        user = UserFactory()
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        Subscription.objects.create(user=user)
        assert Subscription.objects.filter(user=user).exists()

