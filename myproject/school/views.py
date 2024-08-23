from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from .models import School

# Create your views here.
def school(request):
    schools = School.objects.all().values()
    template = loader.get_template('school/schools.html')
    context = {
        'schools':schools,
    }
    return HttpResponse(template.render(context,request))

def school_details(request, id):
    school = School.objects.get(id=id)
    template = loader.get_template('school/school_details.html')
    context = {
        'school': school,
    }
    return HttpResponse(template.render(context, request))

def school_login(request):
    template = loader.get_template('school/school_login.html')
    return HttpResponse(template.render())
    
