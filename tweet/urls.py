from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweets/<int:tweet_id>', views.tweet_detail_view, name='tweet_detail'),
    path('tweets/create', views.tweet_create_view, name='tweet_create'),
]

# URL dispatcher: <int:tweet_id>
# https://docs.djangoproject.com/en/3.1/topics/http/urls/
