from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms 
from .models import Pupil
from django.shortcuts import render, redirect
from .forms import PupilSignupForm


# Create your views here.

def pupil_login(request): 
    return render(request, 'pupil/login.html')

def signup(request):
    if request.method == "POST":
        form = PupilSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pupil_login')  # Redirect after saving
        else:
            print(form.errors)
    else:
        form = PupilSignupForm()
    
    return render(request, 'pupil/signup.html', {'form': form})


def dashboard(request):
    template = loader.get_template('pupil/dashboard.html')
    return HttpResponse(template.render())

