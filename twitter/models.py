from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Twit(models.Model):
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)

    def snippet(self):
        return self.body[:30]+ ' ...'