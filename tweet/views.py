from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import MyUser, post
from tweet.models import posts
from tweet import models
from django.views.generic import DetailView, ListView, CreateView


def index(request, posts_id):
    posts = models.posts.objects.filter(id=posts_id).first()
    return render(request, "posts.html", {"posts": posts})


@login_required()
def ticket_creation_view(request):
    if request.method == "POST":
        ticket = TicketForm(request.POST)
        if ticket.is_valid():
            data = ticket.cleaned_data
            new_ticket = Ticket.objects.create(
                ticket_title=data["title"],
                ticket_description=data["description"],
                ticket_user_who_filed=request.user,
            )
        return HttpResponseRedirect(reverse("homepage"))

    ticket = TicketForm()
    return render(request, "about.html", {"ticket": ticket})
    return render_to_response("index.html", ticket)
