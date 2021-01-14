from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    who_im_following = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False, null=True
    )
