from django.db import models

from twitteruser.models import MyUser


class Notification(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} {self.message}'
        # https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django
