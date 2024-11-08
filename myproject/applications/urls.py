from . import views
from django.urls import path 

urlpatterns = [
    path('application_form/',views.application_form, name ='applicationform'),
    # path('edit_application/<int:application_id>/', views.edit_application, name='edit_application'),
    path('view_applications',views.view_applications,name="view_applications"),
    path('pupil_applications/',views.pupil_applications,name="pupil_applications"),
    path('applications/<int:id>/edit/', views.edit_application, name='edit_application'),
    path('applications/<int:id>/delete/', views.delete_application, name='delete_application'),
    path('accept/<int:application_id>/', views.accept_application, name='accept_application'),
    path('waiting_student_confirmation/',views.waiting_student_confirmation,name = 'waiting_student_confimation'),
    path('confirm_enrollment/<int:application_id>/pupil_applications/', views.confirm_enrollment, name='confirm_enrollment'),
    path('finalize_enrollment/<int:application_id>/', views.finalize_enrollment, name='finalize_enrollment'),
]

