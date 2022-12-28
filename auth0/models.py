from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.core.validators import URLValidator
# Create your models here.
from helpers.models import BaseModel


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    id = models.UUIDField(default=uuid4, editable=False,
                          unique=True, primary_key=True)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField()
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    facebook_url = models.URLField(max_length=200, blank=True, validators=[URLValidator(
        regex='/^(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?$/', message='Invalid Facebook URL',)])
    linkedin_url = models.URLField(
        max_length=200, blank=True, validators=[URLValidator()])
    twitter_url = models.URLField(
        max_length=200, blank=True, validators=[URLValidator()])
    followers = models.ManyToManyField(
        'self', related_name='following', through='Follow')

    def __str__(self):
        return self.user.username
