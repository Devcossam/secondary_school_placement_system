from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('application_form/',views.application_form, name ='applicationform'),
    path('signup/', views.signup, name='signup'),
    path('signup_success/', views.signup_success, name='signup_success'),
]
