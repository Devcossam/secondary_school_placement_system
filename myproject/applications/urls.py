from . import views
from django.urls import path 

urlpatterns = [
    path('application_form/',views.application_form, name ='applicationform'),
    # path('edit_application/<int:application_id>/', views.edit_application, name='edit_application'),
    path('view_applications',views.view_applications,name="view_applications"),
    path('applications/<int:id>/edit/', views.edit_application, name='edit_application'),
    path('applications/<int:id>/delete/', views.delete_application, name='delete_application'),
]

