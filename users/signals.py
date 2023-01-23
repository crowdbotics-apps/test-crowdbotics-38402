from django.db.models.signals import post_save
from django.dispatch import receiver

from test_crowdbotics_38402 import settings
from subscriptions.models import Subscription


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_subscription(sender, instance, created, **kwargs):
    if created:
        Subscription.objects.create(user=instance)
