from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ApplicationForm
from .models import Application
from .forms import ApplicationCheckForm
from django.core.mail import send_mail
from notifications.models import Notification

# def application_form(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             school = form.cleaned_data['school']
#             grade = form.cleaned_data['grade_level']

#             # Check if the school's overall capacity is full
#             if school.total_available_space() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, the school is full at the moment.'
#                 })

#             # Check if the selected grade's capacity is full
#             if grade == 'grade_12' and school.available_space_grade_12() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, Grade 12 is full at the moment.'
#                 })
#             elif grade == 'grade_11' and school.available_space_grade_11() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, Grade 11 is full at the moment.'
#                 })
#             elif grade == 'grade_10' and school.available_space_grade_10() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, Grade 10 is full at the moment.'
#                 })
#             elif grade == 'grade_9' and school.available_space_grade_9() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, Grade 9 is full at the moment.'
#                 })
#             elif grade == 'grade_8' and school.available_space_grade_8() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, Grade 8 is full at the moment.'
#                 })

#             # If there's space, save the application
#             application = form.save(commit=False)
#             application.pupil = request.user.pupil  # Assuming a Pupil model is related to the user
#             application.save()

#             return redirect('/dashboard')  # Redirect after saving

#         else:
#             print(form.errors)
#     else:
#         form = ApplicationForm()

#     return render(request, 'applications/application_form.html', {'form': form})

# def application_form(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES)
#         if form.is_valid():
#             school = form.cleaned_data['school']
#             grade = form.cleaned_data['grade_level']

#             # Check if the school's overall capacity is full
#             if school.total_available_space() == 0:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': 'Sorry, the school is full at the moment.'
#                 })

#             # Check if the selected grade's capacity is full
#             grade_full_error = None
#             if grade == 'grade_12' and school.available_space_grade_12() == 0:
#                 grade_full_error = 'Sorry, Grade 12 is full at the moment.'
#             elif grade == 'grade_11' and school.available_space_grade_11() == 0:
#                 grade_full_error = 'Sorry, Grade 11 is full at the moment.'
#             elif grade == 'grade_10' and school.available_space_grade_10() == 0:
#                 grade_full_error = 'Sorry, Grade 10 is full at the moment.'
#             elif grade == 'grade_9' and school.available_space_grade_9() == 0:
#                 grade_full_error = 'Sorry, Grade 9 is full at the moment.'
#             elif grade == 'grade_8' and school.available_space_grade_8() == 0:
#                 grade_full_error = 'Sorry, Grade 8 is full at the moment.'

#             if grade_full_error:
#                 return render(request, 'applications/application_form.html', {
#                     'form': form,
#                     'error': grade_full_error
#                 })

#             # Save the application
#             application = form.save(commit=False)
#             application.pupil = request.user.pupil  # Assuming Pupil model is related to the user
#             application.save()

#             # Create a notification for the school admin
#             admin_user = school.user  # Access the related User instance
#             if admin_user:
#                 Notification.objects.create(
#                     user=school.admin_user,  # Assuming each school has an 'admin_user'
#                     message=f"A new application from {application.pupil.user.username} has been submitted."
#                 )

#             # Optionally send an email to the school admin
#             send_mail(
#                 subject='New Application Submitted',
#                 message=f"{application.pupil.user.username} has applied to your school.",
#                 from_email='no-reply@schoolplacement.com',
#                 recipient_list=[school.email],
#                 fail_silently=False,
#             )

#             # Create a notification for the student (applicant)
#             Notification.objects.create(
#                 user=request.user,
#                 message=f"You have successfully applied to {school.name}. Your application is under review."
#             )

#             # Optionally send an email to the student
#             send_mail(
#                 subject='Application Submitted',
#                 message=f"Your application to {school.name} has been submitted successfully and is under review.",
#                 from_email='no-reply@schoolplacement.com',
#                 recipient_list=[request.user.email],
#                 fail_silently=False,
#             )

#             # Redirect to the dashboard after submission
#             return redirect('/dashboard')

#         else:
#             print(form.errors)
#     else:
#         form = ApplicationForm()

#     return render(request, 'applications/application_form.html', {'form': form})
@login_required
def application_form(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.cleaned_data['school']
            grade = form.cleaned_data['grade_level']

            if school.total_available_space() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, the school is full at the moment.'
                })

            grade_full_error = None
            if grade == 'grade_12' and school.available_space_grade_12() == 0:
                grade_full_error = 'Sorry, Grade 12 is full at the moment.'
            elif grade == 'grade_11' and school.available_space_grade_11() == 0:
                grade_full_error = 'Sorry, Grade 11 is full at the moment.'
            elif grade == 'grade_10' and school.available_space_grade_10() == 0:
                grade_full_error = 'Sorry, Grade 10 is full at the moment.'
            elif grade == 'grade_9' and school.available_space_grade_9() == 0:
                grade_full_error = 'Sorry, Grade 9 is full at the moment.'
            elif grade == 'grade_8' and school.available_space_grade_8() == 0:
                grade_full_error = 'Sorry, Grade 8 is full at the moment.'

            if grade_full_error:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': grade_full_error
                })

            pupil = getattr(request.user, 'pupil', None)
            if not pupil:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'No pupil associated with this user.'
                })

            application = form.save(commit=False)
            application.pupil = pupil
            application.save()

            # Use the correct field to access the admin user
            admin_user = school.user
            if admin_user:
                Notification.objects.create(
                    user=admin_user,
                    message=f"A new application from {pupil.user.username} has been submitted."
                )

            # Send email to the school admin
            try:
                send_mail(
                    subject='New Application Submitted',
                    message=f"{pupil.user.username} has applied to your school.",
                    from_email='no-reply@schoolplacement.com',
                    recipient_list=[admin_user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email to school: {e}")

            # Create a notification for the student
            Notification.objects.create(
                user=request.user,
                message=f"You have successfully applied to {school.name}. Your application is under review."
            )

            # Send email to the student
            try:
                send_mail(
                    subject='Application Submitted',
                    message=f"Your application to {school.name} has been submitted successfully and is under review.",
                    from_email='no-reply@schoolplacement.com',
                    recipient_list=[request.user.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Failed to send email to student: {e}")

            return redirect('/dashboard')

        else:
            print(form.errors)
    else:
        form = ApplicationForm()

    return render(request, 'applications/application_form.html', {'form': form})


@login_required
def view_applications(request):
    try:
        pupil = request.user.pupil  # Assuming you have pupil linked to the user
        applications = Application.objects.filter(pupil=pupil)  # Get the applications for the pupil

        if applications:
            return render(request, 'applications/list_of_applications.html', {
                'applications': applications,
            })
        
        return render(request,'applications/no_application_found.html')
    
    except AttributeError:
        return render(request, 'applications/no_application_found.html', {'message': 'No pupil associated with this user.'})


def pupil_applications(request):
    school = request.user.school
    pending_applications = Application.objects.filter(school=school, status='Pending')
   
    template = loader.get_template('applications/pupil_applications.html')
    context = {
        'pending_applications': pending_applications,
    }
    return HttpResponse(template.render(context,request))

@login_required
def edit_application(request, id):
    application = get_object_or_404(Application, id=id, pupil=request.user.pupil)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'applications/application_form.html', {'form': form})

@login_required
def delete_application(request, id):
    application = get_object_or_404(Application, id=id, pupil=request.user.pupil)
    if request.method == 'POST':
        application.delete()
        return redirect('/dashboard')
    return render(request, 'delete_confirmation.html', {'application': application})

# @login_required
# def accept_application(request, application_id):
#     application = get_object_or_404(Application, id=application_id)
#     application.status = 'accepted'
#     application.save()
#     return redirect('waiting_student_confirmation')  # Adjust as needed

@login_required
def accept_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    application.status = 'accepted'
    application.save()

    # Notify the student that their application has been accepted
    pupil = application.pupil
    Notification.objects.create(
        user=pupil.user,  # Assuming Pupil has a related User instance
        message=f"Your application to {application.school.name} has been accepted. Please confirm your intent to enroll.",
        application=application  # Assuming Notification has an application ForeignKey field
    )

    # Redirect to a confirmation message view for the school
    return redirect('waiting_student_confirmation')

@login_required
def confirm_enrollment(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if application.status == 'accepted':  # Only proceed if status is "accepted"
        application.status = 'awaiting_confirmation'
        application.save()
    return redirect('student_dashboard')  # Adjust as needed

def waiting_student_confirmation(request):
    template = loader.get_template('applications/waiting_student_confirmation.html')
    return HttpResponse(template.render())

def finalize_enrollment(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if application.status == 'awaiting_confirmation':  # Only proceed if status is "awaiting_confirmation"
        application.status = 'enrolled'
        application.save()
    return redirect('student_dashboard')
