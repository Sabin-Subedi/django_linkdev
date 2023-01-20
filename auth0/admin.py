from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class Users(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")
