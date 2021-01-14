from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/follow', views.follow_user, name='follow_user'),
    path('<int:user_id>',  views.user_profile, name='user_profile'),
]
