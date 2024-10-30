from django.shortcuts import render, get_object_or_404, redirect
from notifications.models import Notification

# Create your views here.
# def notification_list(request):
#     notifications = request.user.notifications.all().order_by('-timestamp')
#     return render(request, 'notifications/notification_list.html', {'notifications': notifications})

# def mark_notification_as_read(request, notification_id):
#     notification = get_object_or_404(Notification, id=notification_id, user=request.user)
#     notification.is_read = True
#     notification.save()
#     return redirect('notification_list')

def student_notifications(request):
    """View for students to see their notifications."""
    notifications = request.user.notifications.all().order_by('-timestamp')
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'dashboard_type': 'student'
    })

def school_notifications(request):
    """View for schools to see their notifications."""
    notifications = request.user.notifications.all().order_by('-timestamp')
    return render(request, 'notifications/notification_list.html', {
        'notifications': notifications,
        'dashboard_type': 'school'
    })

def mark_notification_as_read(request, notification_id):
    """Mark a notification as read."""
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications:student_notifications' if request.user.groups.filter(name='Students').exists() else 'notifications:school_notifications')

