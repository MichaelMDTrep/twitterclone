from django.shortcuts import render

from .models import Notification


def notification_list(request):
    notifications = Notification.objects.filter(
        user=request.user).order_by('-created_at')
    notifications.update(is_new=False)
    return render(request, 'notification/notification_list.html', {'notifications': notifications})
