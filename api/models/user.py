from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models.user_manager import UserManager


class User(AbstractUser):
    # https://docs.djangoproject.com/en/2.0/ref/models/options/#app-label
    app_label = 'api'
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
