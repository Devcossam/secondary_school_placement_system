from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 

# Create your views here.
def school(request):
    template = loader.get_template('school/schools.html')
    return HttpResponse(template.render())
    
