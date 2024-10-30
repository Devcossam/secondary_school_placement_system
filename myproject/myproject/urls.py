"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from pupil import views as pupil_views
from school import views as school_views
from applications import views as application_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name='home'),
    path('pupil_login/',pupil_views.pupil_login, name='pupil_login'),
    path('school_login/',school_views.school_login, name='school_login'),
    path('about/',views.about, name='about'),
    path('school/',school_views.school, name='schools'),
    path('school/school_details/<int:id>',school_views.school_details,name="school_details"),
    path('signup/',pupil_views.signup, name='signup'),
    path('update_information',pupil_views.update_information,name='update_information'),
    path('dashboard/',pupil_views.dashboard,name='dashboard'),
    path('school_dashboard/',school_views.school_dashboard,name="school_dashboard"),
    path('school_signup/',school_views.school_signup,name="school_signup"),
    path('pupil_applications/',school_views.pupil_applications,name="pupil_applications"),
    path('school_search/',school_views.school_search,name="school_search"),
    path('application_form/',application_views.application_form,name="applicationform"),
    path('view_applications/',application_views.view_applications,name="view_applications"),
    path('applications/<int:id>/edit/', application_views.edit_application, name='edit_application'),
    path('applications/<int:id>/delete/', application_views.delete_application, name='delete_application'),
    # path('edit_application/<int:application_id>/',application_views.edit_application,name="edit_application"),
    # path('rate/<int:school_id>/', school_views.rate_school, name='rate_school'),
    path('top_rated_schools/', school_views.top_rated_schools, name='top_schools'),
    path('school/<int:school_id>/', school_views.school_ratings, name='school_ratings'),
    path('school/<int:school_id>/rate/', school_views.rate_school, name='rate_school'),
    path('notifications/', include('notifications.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
