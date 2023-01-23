
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ApplicationViewSet

router = DefaultRouter()
router.register('apps', ApplicationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
