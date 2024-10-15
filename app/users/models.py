from django.db import models
from django.contrib.auth.models import AbstractUser

from base.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    public_key = models.CharField(max_length=256, unique=True, null=True)

    def __str__(self):
        return self.public_key
