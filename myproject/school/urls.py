from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.school, name='school'),
    path('school/school_details/<int:id>',views.school_details, name='school_details'),
]
