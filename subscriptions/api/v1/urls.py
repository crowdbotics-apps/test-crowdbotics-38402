
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SubscriptionViewSet
router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
