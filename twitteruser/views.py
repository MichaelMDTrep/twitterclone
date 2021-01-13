from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from twitteruser.forms import SignUpForm
from twitteruser.models import MyUser
from twitteruser.models import Tweet


def index(request):
    Tweets = Tweet.objects.all().order_by("-id")
    return render(
        request,
        "index.html",
        {"twitterapp": Tweets}
    )


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                age=data.get("age"),
            )
            login(request, newuser)
        return HttpResponseRedirect(reverse("homepage"))

    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})
