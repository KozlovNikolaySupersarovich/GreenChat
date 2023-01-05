from django.db import models
from user.models import CustomUser
from datetime import datetime


class Message(models.Model):
    author = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    text = models.CharField(max_length=500, null=False)
    sent_time = models.DateTimeField(default=datetime.now)
