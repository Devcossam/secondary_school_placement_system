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
            form.save()
            return redirect('/dashboard')  # Redirect after saving
        else:
            print(form.errors)
    else:
        form = ApplicationForm()
    
    return render(request, 'applications/application_form.html', {'form': form})

# def view_application_status(request, application_id):
#     application = get_object_or_404(Application, id=application_id)
#     return render(request, 'view_application_status.html',{'application':application})

 
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

# def check_application_status(request):
#     # Fetch the pupil related to the logged-in user
#     pupil = request.user.pupil  # Adjust based on how you've set up user relationships

#     # Fetch the application associated with the pupil
#     application = Application.objects.filter(pupil=pupil).first()

#     if application:
#         return redirect('view_application_status', application_id=application.id)

#     return render(request, 'applications/no_application_found.html')  # Template for no application case

# def check_application_status(request):
#     if request.method == 'POST':
#         form = ApplicationCheckForm(request.POST)
#         if form.is_valid():
#             application_id = form.cleaned_data['application_id']
#             return redirect('view_application_status', application_id=application_id)
#     else:
#         form = ApplicationCheckForm()
    
#     return render(request, 'check_application_status.html', {'form': form})
