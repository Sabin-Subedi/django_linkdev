from rest_framework import routers
from django.urls import path
from . import views


router = routers.SimpleRouter()

# router.register("users/profile", views.ProfileViewSet, basename="users-profile")


urlpatterns = [
    path("users/check-username/", views.check_username, name="check_username"),
    path("users/profile/me/", views.get_profile, name="get_profile")
] + router.urls
