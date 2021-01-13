from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import MyUser


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = [
            "first_name",
            "last_name",
            "age",
        ]
