from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('schools/',views.school, name='school'),
    path('school_login/',views.school_login, name='school_login'),
    path('schools/school_details/<int:id>/',views.school_details, name="school_details"),
    path('school_dashboard/',views.school_dashboard,name="school_dashboard"),
]
