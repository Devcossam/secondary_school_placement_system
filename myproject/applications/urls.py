from . import views
from django.urls import path 

urlpatterns = [
    path('application_form/',views.application_form, name ='applicationform'),
    # path('application/<int:application_id>/',views.view_application_status, name='view_application_status'),
    path('check-status/', views.check_application_status, name='check_application_status'),
]
