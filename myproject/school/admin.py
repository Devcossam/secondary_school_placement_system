from django.contrib import admin
from .models import School
from .models import Rating

# Register your models here.
admin.site.register(School)
admin.site.register(Rating)
