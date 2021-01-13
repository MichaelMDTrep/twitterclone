from django.db import models
from django.utils import timezone
from twitteruser.models import MyUser


class posts(models.Model):
    posts = models.TextField(max_length=300)
    time_date = models.DateTimeField(default=timezone.now)
    my_user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="posts")
