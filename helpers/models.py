from django.db import models
import uuid
# Create your models here.


class BaseModel(models.Model):
    idx = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    is_obsolete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
