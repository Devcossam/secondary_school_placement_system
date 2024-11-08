from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pupil_login/',views.pupil_login, name="pupil_login"),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('signup/',views.signup, name='signup'),
    path('update_information/',views.update_information,name="update_information"),
    path('confirm_enrollment/',views.confirm_enrollment,name='confirm_enrollment'),
    path('confirmation_success/',views.confirmation_success,name = 'confirmation_success'),
]
