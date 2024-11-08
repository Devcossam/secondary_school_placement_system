from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.template import loader 
from .models import School
from .models import Rating
from django.contrib.auth.forms import UserCreationForm
from .forms import SchoolSearchForm
from .forms import SchoolSignupForm
from .forms import RatingForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from applications.models import Application
from django.db.models import Avg
from django.contrib import messages
from notifications.models import Notification


# Create your views here.
def school(request):
    schools = School.objects.all().values()
    template = loader.get_template('school/schools.html')
    context = {
        'schools':schools,
    }
    return HttpResponse(template.render(context,request))


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
    pending_applications = Application.objects.filter(school=school, status='Pending')
    pending_count = pending_applications.count() 
    return render(request,"school/school_dashboard.html",{
        'school':school,
        'pending_applications': pending_applications,
        'pending_count': pending_count,
        })

def school_search(request):
    form = SchoolSearchForm()
    results = []

    if request.method == 'GET':
        form = SchoolSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = School.objects.filter(name__icontains=query)

    return render(request, 'school/school_search.html', {'form': form, 'results': results})


# @login_required
# def rate_school(request, school_id):
#     school = get_object_or_404(School, pk=school_id)
#     # rating, created = Rating.objects.get_or_create(user=request.user, school=school)
    
#     if request.method == 'POST':
#         form = RatingForm(request.POST, instance=rating)
#     #     if form.is_valid():
#     #         form.save()
#     #         return redirect('school/school_detail', school_id=school.id)
#     # else:
#         # form = RatingForm(instance=rating)

#     return render(request, 'school/rate_school.html', {'school': school})

def top_rated_schools(request):
    top_schools = School.get_top_rated_schools()
    return render(request, 'school/top_rated_schools.html', {'top_schools': top_schools})

def school_ratings(request, school_id):
    school = get_object_or_404(School, id=school_id)
    ratings = school.ratings.all()
    user_rating = None

    if request.user.is_authenticated:
        try:
            user_rating = Rating.objects.get(school=school, user=request.user)
        except Rating.DoesNotExist:
            pass

    context = {
        'school': school,
        'ratings': ratings,
        'user_rating': user_rating,
    }

    return render(request, 'school/school_ratings.html', context)

# @login_required
# def rate_school(request, school_id):
#     school = get_object_or_404(School, id=school_id)

#     try:
#         rating = Rating.objects.get(school=school, user=request.user)
#     except Rating.DoesNotExist:
#         rating = None

#     if request.method == 'POST':
#         form = RatingForm(request.POST, instance=rating)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.user = request.user
#             rating.school = school
#             rating.save()
#             return redirect('school/<int:school_id>/', school_id=school.id)
#     else:
#         form = RatingForm(instance=rating)

#     return render(request, 'school/rate_school.html', {'form': form, 'school': school})

@login_required
def rate_school(request, school_id):
    school = get_object_or_404(School, id=school_id)

    # Check if the user has already rated the school
    try:
        rating = Rating.objects.get(school=school, user=request.user)
        already_rated = True
    except Rating.DoesNotExist:
        rating = None
        already_rated = False

    if request.method == 'POST':
        # Use the existing rating if editing
        form = RatingForm(request.POST, instance=rating)  
        if form.is_valid():
            # Save the new or updated rating
            rating = form.save(commit=False)
            rating.user = request.user
            rating.school = school
            rating.save()
            messages.success(request, 'Your rating has been submitted successfully.')
            return redirect('rate_school', school_id=school.id)

    else:
        # On GET request, show the form with existing rating for editing
        form = RatingForm(instance=rating) if already_rated else RatingForm()

    context = {
        'form': form,
        'school': school,
        'already_rated': already_rated
    }
    return render(request, 'school/rate_school.html', context)

@login_required
def finalize_enrollment(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    # Ensure only the school can finalize the enrollment
    if request.user != application.school.user:
        return redirect('home')  # Redirect unauthorized users

    # Update application status to 'enrolled'
    application.status = 'enrolled'
    application.save()

    # Optionally, notify the student that they have been fully enrolled
    Notification.objects.create(
        user=application.pupil.user,
        message=f"You have been fully enrolled in {application.school.name}.",
        application = application
    )

    return redirect('finalize_success')


def finalize_success(request):
    template = loader.get_template('school/finalize_success.html')
    return HttpResponse(template.render())

