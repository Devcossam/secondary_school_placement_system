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
    path('dashboard/',pupil_views.dashboard,name='dashboard'),
    path('school_dashboard/',school_views.school_dashboard,name="school_dashboard"),
    path('school_search/',school_views.school_search,name="school_search"),
    path('application_form/',application_views.application_form,name="applicationform"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
