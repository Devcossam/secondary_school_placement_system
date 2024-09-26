from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms 
from .models import Pupil
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Saving the new student to the database
            return redirect('/login')  # Redirect to a success page or another view
    else:
        form = StudentSignUpForm()
    template = loader.get_template('pupil/signup.html')
    return HttpResponse(template.render({'form':form}))

def dashboard(request):
    template = loader.get_template('pupil/dashboard.html')
    return HttpResponse(template.render())

def application_form(request):
    template = loader.get_template('pupil/application_form.html')
    return HttpResponse(template.render())