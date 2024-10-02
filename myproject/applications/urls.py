from . import views
from django.urls import path 

urlpatterns = [
    path('application_form/',views.application_form, name ='applicationform'),
    # path('edit_application/<int:application_id>/', views.edit_application, name='edit_application'),
    path('check-status/', views.check_application_status, name='check_application_status'),
    path('view_applications',views.view_applications,name="view_applications")
]
