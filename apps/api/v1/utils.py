import uuid

from apps.api.v1.serializers import ApplicationSerializer
from apps.models import Applications
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


def generate_random_app_name(request):
    random_uuid = "-" + str(uuid.uuid4())
    request.data["name"] += random_uuid
    return request.data["name"]


def check_subscription_plan(subscription, request):
    if subscription.plan.name == "FREE" and subscription.applications_set.all().count() > 0:
        app_data = {"data": f"The {subscription.plan.name} plan, only allows you to create 1 Application,"
                            f"update your plan to create more Applications."}
        status_code = HTTP_200_OK
    else:
        app = Applications.objects.create(name=generate_random_app_name(request),
                                          description=request.data["description"],
                                          type=request.data["type"],
                                          framework=request.data["framework"],
                                          domain_name=request.data["domain_name"],
                                          subscription=subscription)
        app_data = ApplicationSerializer(app).data
        status_code = HTTP_201_CREATED

    return app_data, status_code
