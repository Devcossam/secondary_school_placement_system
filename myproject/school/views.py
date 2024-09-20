from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader 
from .models import School
from django.contrib.auth.forms import UserCreationForm
from .forms import SchoolSearchForm

# Create your views here.
def school(request):
    schools = School.objects.all().values()
    template = loader.get_template('school/schools.html')
    context = {
        'schools':schools,
    }
    return HttpResponse(template.render(context,request))

def school_login(request):
    template = loader.get_template('school/school_login.html')
    return HttpResponse(template.render())

def school_details(request, id):
    school = School.objects.get(id=id)
    template = loader.get_template('school/details.html')
    context = {
        'school': school,
    }
    return HttpResponse(template.render(context, request))

def school_dashboard(request):
    template = loader.get_template('school/school_dashboard.html')
    return HttpResponse(template.render())


def school_search(request):
    form = SchoolSearchForm()
    results = []

    if request.method == 'GET':
        form = SchoolSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = School.objects.filter(name__icontains=query)

    return render(request, 'school/school_search.html', {'form': form, 'results': results})