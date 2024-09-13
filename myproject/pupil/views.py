from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django import forms 
from .models import Pupil
from django.shortcuts import render, redirect

def pupil_login(request): 
    return render(request, 'pupil/login.html')

def landing_page(request):
    return render(request, 'pupils/dashboard.html')

# Create your views here.
def signup(request):
    template = loader.get_template('pupil/signup.html')
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('pupil/dashboard.html')
    return HttpResponse(template.render())

