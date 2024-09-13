from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .forms import ApplicationForm

def application_form(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')  # Redirect after saving
        else:
            print(form.errors)
    else:
        form = ApplicationForm()
    
    return render(request, 'applications/application_form.html', {'form': form})


# def application_form(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST) 
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you for your application!")
#     else:
#         form = ApplicationForm() 
    
#     template = loader.get_template('applications/application_form.html')
#     return HttpResponse(template.render({'form': form}, request))
