from django.db import models
from twitteruser.models import MyUser


class Tweet(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='tweets')
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    # Auto Now Add: https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField.auto_now_add
