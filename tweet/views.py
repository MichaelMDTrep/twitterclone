# render: https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#the-save-method
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, CreateView

from twitteruser.models import MyUser
from .models import Tweet
from .forms import TweetForm


@login_required
def home(request):
    tweets = Tweet.objects.all().order_by('-id')
    return render(request, 'home.html', {'tweets': tweets})


def tweet_detail_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, "tweet_detail.html", {"tweet": tweet})


@login_required
def tweet_create_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            # save(commit=False): https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#the-save-method
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})
