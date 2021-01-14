from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    who_im_following = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False)

    @property
    def new_notifications(self):
        """Returns total number of the user's notifications that have an is_new value of True"""
        # Count: https://stackoverflow.com/questions/5439901/getting-a-count-of-objects-in-a-queryset-in-django
        return self.notifications.filter(is_new=True).count()
