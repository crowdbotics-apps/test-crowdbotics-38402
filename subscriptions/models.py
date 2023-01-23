from users.models import User
from django.db import models


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name="subscription_user")
    active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    update_at = models.DateTimeField("Update at", auto_now_add=True)