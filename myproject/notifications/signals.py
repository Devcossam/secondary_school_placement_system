from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from applications.models import Application  # Assuming your application model is in applications app
from notifications.models import Notification

@receiver(post_save, sender=Application)
def create_notifications(sender, instance, created, **kwargs):
    if created:
        # Notify the school about the new application
        Notification.objects.create(
            user=instance.school.user,  # Assuming schools have an admin user field
            message=f"A new application from {instance.pupil.user.username} has been submitted.",
        )

        # Optionally, send an email to the school
        send_mail(
            subject='New Application Submitted',
            message=f"{instance.pupil.user.username} has applied to your school.",
            from_email='no-reply@schoolplacement.com',
            recipient_list=[instance.school.email],
            fail_silently=False,
        )
    else:
        # Notify the student when the status of the application changes
        Notification.objects.create(
            user=instance.pupil.user,
            message=f"Your application status is now: {instance.get_status_display()}",
        )
                    

        # Optionally, send an email to the student
        send_mail(
            subject='Application Status Update',
            message=f"Your application to {instance.school.name} is now {instance.get_status_display()}.",
            from_email='no-reply@schoolplacement.com',
            recipient_list=[instance.pupil.email],
            fail_silently=False,
        )
