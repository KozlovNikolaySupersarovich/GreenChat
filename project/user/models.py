from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.username)
