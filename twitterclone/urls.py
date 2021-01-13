"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as twitteruser_views
from authentication import views as authentication_views

urlpatterns = [
    path("", twitteruser_views.index, name="homepage"),
    path('login/', authentication_views.login_view, name='login'),
    path('logout/', authentication_views.user_logout, name='logout'),
    path("sign_up/", twitteruser_views.sign_up, name="sign_up"),
    path('admin/', admin.site.urls),
]
