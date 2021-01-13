from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import MyUser

from .models import MyUser

admin.site.register(MyUser, UserAdmin)
