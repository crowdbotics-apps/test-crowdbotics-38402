import pytest

from subscriptions.models import Subscription
from users.models import User

pytestmark = pytest.mark.django_db


class TestSignal:
    def test_create_subscription_when_user_is_created(self):
        user = User.objects.create(name="test")
        assert Subscription.objects.filter(user=user).count() == 1
