from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms 
from .models import Pupil
from django.shortcuts import render, redirect
from .forms import PupilSignupForm
from .forms import PupilUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



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
            form.save()  # Save the new student to the database
            return redirect('/login')  # Redirect to a success page or another view
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
    

