from django.urls import path
from .views import student_notifications, school_notifications, mark_notification_as_read

app_name = 'notifications'

urlpatterns = [
    path('student/', student_notifications, name='student_notifications'),
    path('school/', school_notifications, name='school_notifications'),
    path('read/<int:notification_id>/', mark_notification_as_read, name='mark_notification_as_read'),
]