from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=12, blank=True)
