from django.contrib import admin
from django.urls import path, include

from twitteruser import views as twitteruser_views
from authentication import views as authentication_views

urlpatterns = [
    path('', include('tweet.urls')),
    path('users/', include('twitteruser.urls')),
    path('notifications/', include('notification.urls')),
    path('login/', authentication_views.login_view, name='login'),
    path('logout/', authentication_views.user_logout, name='logout'),
    path("sign_up/", twitteruser_views.sign_up, name="sign_up"),
    path('admin/', admin.site.urls),
]
