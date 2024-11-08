from django.db import models
from django.contrib.auth.models import User
from applications.models import Application

# Create your models here


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    application = models.ForeignKey(Application, null=True, blank=True, on_delete=models.CASCADE)  # Link to Application

    class Meta:
        db_table = 'notification'

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}"
