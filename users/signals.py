from django.db.models.signals import post_save
from django.dispatch import receiver

from plans.models import Plan
from test_crowdbotics_38402 import settings
from subscriptions.models import Subscription


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_subscription(sender, instance, created, **kwargs):
    if created:
        plan = Plan.objects.filter(name="FREE").first()
        if not plan:
            Subscription.objects.create(
                                user=instance,
                                plan=Plan.objects.create(
                                    name="FREE",
                                    description="FREE PLAN",
                                    price=0))

