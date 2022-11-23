from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUsers(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users_user'
        app_label = 'users'
