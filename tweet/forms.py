# Model Forms: https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/
from django.forms import ModelForm

from .models import Tweet


class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['text']
