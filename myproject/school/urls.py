from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('schools/',views.school, name='school'),
    path('school_login/',views.school_login, name='school_login'),
    path('school_signup/',views.school_signup,name="school_signup"),
    path('schools/school_details/<int:id>/',views.school_details, name="school_details"),
    path('school_dashboard/',views.school_dashboard,name="school_dashboard"),
    path('search/', views.school_search, name='school_search'),
    # path('rate/<int:school_id>/', views.rate_school, name='rate_school'),
    path('top_rated_schools/', views.top_rated_schools, name='top_schools'),
    path('school/<int:school_id>/', views.school_ratings, name='school_ratings'),
    path('school/<int:school_id>/rate/', views.rate_school, name='rate_school'),
    path('finalize_enrollment/<int:application_id>/', views.finalize_enrollment, name='finalize_enrollment'),
    path('finalize_success/',views.finalize_success,name='finalize_success'),
]
