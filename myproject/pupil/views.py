from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms 
from .models import Pupil
from django.shortcuts import get_object_or_404
from .forms import PupilSignupForm
from .forms import PupilUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from applications.models import Application
from notifications.models import Notification
from django.core.mail import send_mail



# Create your views here.

def pupil_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use get to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Use the name of the URL pattern without trailing slash
        else:
            return render(request, 'pupil/login.html', {'error': 'Invalid Username or Password'})
    
    return render(request, 'pupil/login.html')


def signup(request):
    if request.method == "POST":
        form = PupilSignupForm(request.POST)
        if form.is_valid():
            pupil = form.save()
            login(request, pupil.user)  # Log the user in
            return redirect('/pupil_login')  # Redirect after saving
    else:
        form = PupilSignupForm()
    
    return render(request, 'pupil/signup.html', {'form': form})


@login_required
def dashboard(request):
    pupil = request.user.pupil  # Access the related Pupil instance
    return render(request, 'pupil/dashboard.html', {'pupil': pupil})

@login_required
def update_information(request):
    pupil = request.user.pupil  # Get the pupil instance
    if request.method == "POST":
        form = PupilUpdateForm(request.POST, instance=pupil)
        if form.is_valid():
            form.save()  # Save the updated information
            return redirect('/dashboard')  # Redirect to the dashboard or a success page
    else:
        form = PupilUpdateForm(instance=pupil)  # Prepopulate the form with current pupil data

    return render(request, 'pupil/update_information.html', {'form': form})

# @login_required
# def confirm_enrollment(request, application_id):
#     application = get_object_or_404(Application, id=application_id)

#     # Ensure only the student who received the acceptance can confirm
#     if request.user != application.pupil.user:
#         return redirect('home')  # Redirect unauthorized users

#     # Update application status to 'awaiting confirmation'
#     application.status = 'awaiting confirmation'
#     application.save()

#     # Notify the school that the student has confirmed
#     Notification.objects.create(
#         user=application.school.user,  # Assuming School has a related User instance
#         message=f"{application.pupil.name} has confirmed their intent to enroll."
#     )

#     return redirect('confirmation_success')

@login_required
def confirm_enrollment(request, application_id):
    # Fetch the application object by its ID or raise a 404 error if not found
    application = get_object_or_404(Application, id=application_id)

    # Ensure only the student who received the acceptance can confirm
    if request.user != application.pupil.user:
        return redirect('home')  # Redirect unauthorized users to the home page

    # Update the application status to "awaiting confirmation"
    application.status = 'awaiting confirmation'
    application.save()

    # Notify the school that the student has confirmed their intent to enroll
    Notification.objects.create(
        user=application.school.user,  # Assuming the school has a related User instance
        message=f"{application.pupil.name} has confirmed their intent to enroll.",
        application=application  # Link this notification to the specific application
    )

    # Optionally, send an email to the school to inform them of the student's confirmation
    send_mail(
        subject=f"Confirmation Received from {application.pupil.name}",
        message=f"The student {application.pupil.name} has confirmed their intent to enroll at your school.",
        from_email='no-reply@schoolplacement.com',
        recipient_list=[application.school.email],
        fail_silently=False,
    )

    # Redirect to a confirmation success page, or a dashboard
    return redirect('confirmation_success')  # Adjust this to your success page URL


def confirmation_success(request):
    template = loader.get_template('pupil/confirmation_success.html')
    return HttpResponse(template.render())
    

