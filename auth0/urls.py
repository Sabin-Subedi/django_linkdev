from rest_framework import routers
from django.urls import path
from . import views
from . import serializers


router = routers.SimpleRouter()

router.register(r"profile", views.ProfileViewSet, basename="user")

urlpatterns = [
    path("users/check-username/", views.check_username, name="check_username")
] + router.urls
