from django.db import models
from twitteruser.models import MyUser


class Tweet(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='tweets')
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    # Auto Now Add: https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField.auto_now_add

    def __str__(self):
        return f'{self.user}: {self.text} {self.created_at_clean}'
        # https://stackoverflow.com/questions/45483417/what-is-doing-str-function-in-django

    # @property: https://stackoverflow.com/questions/58558989/what-does-djangos-property-do

    @property
    def created_at_clean(self):
        # strftime: https://docs.python.org/3/library/datetime.html#datetime.date.strftime
        # format codes: https://docs.python.org/3/library/datetime.html#datetime.date.strftime
        return self.created_at.strftime('%#m/%#d/%Y %#I:%M %p')
