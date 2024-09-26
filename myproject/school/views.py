from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader 
from .models import School
from django.contrib.auth.forms import UserCreationForm
from .forms import SchoolSearchForm
from .forms import SchoolSignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def school(request):
    schools = School.objects.all().values()
    template = loader.get_template('school/schools.html')
    context = {
        'schools':schools,
    }
    return HttpResponse(template.render(context,request))

# def school(request):
#     form = SchoolSearchForm(request.GET or None)  # Initialize the form with GET data
#     schools = School.objects.all()  # Default to showing all schools
#     results = schools  # This will be used to display either all or filtered results

#     if form.is_valid():  # If form is valid (i.e., it has search input)
#         query = form.cleaned_data.get('query')  # Get the search input from the form
#         if query:  # If there is a search query, filter the schools
#             results = schools.filter(name__icontains=query)

#     context = {
#         'form': form,        # Pass the search form to the template
#         'schools': results,  # Either all schools or the filtered list (search results)
#     }

    # return render(request, 'school/schools.html', context)

def school_signup(request):
    if request.method == "POST":
        form = SchoolSignupForm(request.POST)
        if form.is_valid():
            school = form.save()
            login(request, school.user)  # Log the user in
            return redirect('/school_login')  # Redirect after saving
    else:
        form = SchoolSignupForm()
    
    return render(request, 'school/school_signup.html', {'form': form})


def school_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use get to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('school_dashboard')  # Use the name of the URL pattern without trailing slash
        else:
            return render(request, 'school/school_login.html', {'error': 'Invalid School Name or Password'})
    
    return render(request, 'school/school_login.html')

def school_details(request, id):
    school = School.objects.get(id=id)
    template = loader.get_template('school/details.html')
    context = {
        'school': school,
    }
    return HttpResponse(template.render(context, request))

@login_required
def school_dashboard(request):
    school = request.user.school
    return render(request,"school/school_dashboard.html",{'school':school})

def school_search(request):
    form = SchoolSearchForm()
    results = []

    if request.method == 'GET':
        form = SchoolSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = School.objects.filter(name__icontains=query)

    return render(request, 'school/school_search.html', {'form': form, 'results': results})