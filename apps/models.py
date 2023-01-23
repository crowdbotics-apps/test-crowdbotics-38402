from django.db import models
from subscriptions.models import Subscription


class Applications(models.Model):
    DJANGO = 'Django'
    REACT = 'React'

    APP_FRAMEWORKS = [
        ("DJANGO", 'Django'),
        ("REACT", 'React'),
    ]

    WEB = "Web"
    MOBILE = "Mobile"

    APP_TYPES = [
        ("WEB", 'Web'),
        ("MOBILE", 'Mobile'),
    ]
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    name = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=False, max_length=255, )
    type = models.CharField(blank=False, choices=APP_TYPES, default="None", max_length=50, )
    framework = models.CharField(blank=False, choices=APP_FRAMEWORKS, default="None", max_length=50, )
    domain_name = models.CharField(blank=False, max_length=50)
