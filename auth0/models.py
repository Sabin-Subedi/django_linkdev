from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    id = models.UUIDField(default=uuid4, editable=False,
                          unique=True, primary_key=True)
