from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class Users(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")


@admin.register(models.Profile)
class Profiles(admin.ModelAdmin):
    list_display = (
        "idx",
        "user",
        "bio",
        "profile_picture",
        "location",
        "birth_date",
        "facebook_url",
        "linkedin_url",
        "twitter_url",
    )
