from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pupil_login/',views.pupil_login, name="pupil_login"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
]
