from . import views
from django.urls import path 

urlpatterns = [
    path('application_form/',views.application_form, name ='applicationform'),
]
