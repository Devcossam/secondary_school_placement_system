from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pupil
# Register your models here.


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number')