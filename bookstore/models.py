from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.user.username
