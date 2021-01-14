from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from twitteruser.forms import SignUpForm
from twitteruser.models import MyUser


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
        return HttpResponseRedirect(reverse("home"))

    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})


def user_profile(request, user_id):
    user = MyUser.objects.get(id=user_id)
    return render(request, 'twitteruser/profile.html', {'user': user})


def follow_user(request, user_id):
    user = request.user
    follow_user = MyUser.objects.get(id=user_id)
    if follow_user not in user.who_im_following.all():
        user.who_im_following.add(follow_user)
    else:
        user.who_im_following.remove(follow_user)
    # Same Page: https://stackoverflow.com/questions/26798623/how-to-return-the-result-on-same-page-in-django
    return redirect(request.META['HTTP_REFERER'])
