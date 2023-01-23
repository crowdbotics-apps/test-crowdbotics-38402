import pytest
from rest_framework.status import HTTP_200_OK

from plans.models import Plan
from subscriptions.models import Subscription
from users.models import User
from apps.api.v1.utils import check_subscription_plan
from apps.models import Applications
pytestmark = pytest.mark.django_db


class TestAppsUtils:

    def test_subscription_plan_free(self):
        user = User.objects.create(name="test")
        plan = Plan.objects.create(name="FREE",price=1.00, description="test description")
        subscription = Subscription.objects.create(user=user, plan=plan)
        app_data, status_code = check_subscription_plan(subscription)
        Applications.objects.create(
                                    name="test",
                                    description="test",
                                    type="WEB",framework="DJANGO",
                                    domain_name="test-web")
        assert app_data == {"data": f"The {subscription.plan.name} plan, only allows you to create 1 Application,"
                            f"update your plan to create more Applications."}
        assert status_code == HTTP_200_OK
