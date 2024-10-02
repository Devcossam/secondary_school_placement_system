from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ApplicationForm
from .models import Application
from .forms import ApplicationCheckForm

def application_form(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            school = form.cleaned_data['school']
            grade = form.cleaned_data['grade_level']

            # Check if the school's overall capacity is full
            if school.total_available_space() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, the school is full at the moment.'
                })

            # Check if the selected grade's capacity is full
            if grade == 'grade_12' and school.available_space_grade_12() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, Grade 12 is full at the moment.'
                })
            elif grade == 'grade_11' and school.available_space_grade_11() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, Grade 11 is full at the moment.'
                })
            elif grade == 'grade_10' and school.available_space_grade_10() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, Grade 10 is full at the moment.'
                })
            elif grade == 'grade_9' and school.available_space_grade_9() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, Grade 9 is full at the moment.'
                })
            elif grade == 'grade_8' and school.available_space_grade_8() == 0:
                return render(request, 'applications/application_form.html', {
                    'form': form,
                    'error': 'Sorry, Grade 8 is full at the moment.'
                })

            # If there's space, save the application
            application = form.save(commit=False)
            application.pupil = request.user.pupil  # Assuming a Pupil model is related to the user
            application.save()

            return redirect('/dashboard')  # Redirect after saving

        else:
            print(form.errors)
    else:
        form = ApplicationForm()

    return render(request, 'applications/application_form.html', {'form': form})


# @login_required
# def edit_application(request, application_id):
#     print(f"Requested application ID: {application_id}")
    
#     # Get the application object that the pupil wants to edit
    
#     application = get_object_or_404(Application, id=application_id, pupil=request.user.pupil)
#     print("passed")
#     # Prevent edits if the application has been accepted or rejected (optional)
#     if application.status in ['Accepted', 'Rejected']:
#         return render(request, 'applications/application_form.html', {
#             'error': 'You cannot edit an application that has already been processed.'
#         })

#     if request.method == "POST":
#         form = ApplicationForm(request.POST, request.FILES, instance=application)
#         if form.is_valid():
#             form.save()  # Save the edited application
#             return redirect('/dashboard')  # Redirect to a dashboard or status page
#         else:
#             print(form.errors)
#     else:
#         # Prepopulate the form with the existing application data
#         form = ApplicationForm(instance=application)

#     return render(request, 'applications/application_form.html', {
#         'form': form,
#         "application":application,
#         })

@login_required
def view_applications(request):
    pupil = request.user.pupil  # Assuming you have pupil linked to the user
    applications = Application.objects.filter(pupil=pupil)  # Get the applications for the pupil
    return render(request, 'applications/list_of_applications.html', {
        'applications': applications,
    })

 
@login_required
def check_application_status(request):
    try:
        pupil = request.user.pupil  # Assuming each user has a related Pupil
        application = Application.objects.filter(pupil=pupil).first()

        if application:
            return render(request, 'applications/application_status.html', {'application': application})

        return render(request, 'applications/no_application_found.html')

    except AttributeError:
        return render(request, 'applications/no_application_found.html', {'message': 'No pupil associated with this user.'})

