from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Pupil
from .models import School

# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    return  HttpResponse(template.render()) 

def schools(request):
    template = loader.get_template('all_schools.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def pupils(request):
    mypupils = Pupil.objects.all().values()
    template = loader.get_template('all_pupils.html')
    context = {
        'mypupils': mypupils,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mypupil = Pupil.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mypupil': mypupil,
    }
    return HttpResponse(template.render(context, request))

def school_details(request, id):
    school = School.objects.get(id=id)
    template = loader.get_template('school_details.html')
    context = {
        'school': school,
    }
    return HttpResponse(template.render(context, request))


def testing(request):
    mypupils = Pupil.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        "mypupils": mypupils,
        "emptytest":[],
        }
    return HttpResponse(template.render(context, request))



# from django.shortcuts import render, redirect 
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
# from django.contrib.auth import login, logout

# # Create your views here.
# def register_view(request):
#     if request.method == "POST": 
#         form = UserCreationForm(request.POST) 
#         if form.is_valid(): 
#             login(request, form.save())
#             return redirect("posts:list")
#     else:
#         form = UserCreationForm()
#     return render(request, "users/register.html", { "form": form })

# def login_view(request): 
#     if request.method == "POST": 
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid(): 
#             login(request, form.get_user())
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect("posts:list")
#     else: 
#         form = AuthenticationForm()
#     return render(request, "users/login.html", { "form": form })

# def logout_view(request):
#     if request.method == "POST": 
#         logout(request) 
#         return redirect("posts:list")