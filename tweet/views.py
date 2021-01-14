import re
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# render: https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#the-save-method
from django.shortcuts import render, reverse, redirect, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView

from twitteruser.models import MyUser
from notification.models import Notification
from .models import Tweet
from .forms import TweetForm


@login_required
def home(request):
    user = request.user
    # Q: https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
    tweets = Tweet.objects.filter(Q(user=user) | Q(
        user__in=user.who_im_following.all())).order_by('-created_at')
    return render(request, 'tweet/home.html', {'tweets': tweets})


def tweet_detail_view(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, "tweet/tweet_detail.html", {"tweet": tweet})


@login_required
def tweet_create_view(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            # save(commit=False): https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/#the-save-method
            tweet = form.save(commit=False)
            # regex: https://docs.python.org/3/howto/regex.html
            tweet_message = tweet.text
            pattern = '@([^\s]+)'
            match = re.compile(pattern).search(tweet_message)
            if match:
                mentioned_username = match.group(1)
                try:
                    mentioned_user = MyUser.objects.get(
                        username=mentioned_username)
                    # Model.objects.create: https://docs.djangoproject.com/en/3.1/ref/models/relations/#django.db.models.fields.related.RelatedManager.create
                    Notification.objects.create(
                        user=mentioned_user,
                        message=f'{request.user} mentioned you in their tweet.'
                    )
                except:
                    pass
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    form = TweetForm()
    return render(request, 'tweet/tweet_form.html', {'form': form})
