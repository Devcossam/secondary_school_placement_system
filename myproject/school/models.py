from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    province = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    student_capacity = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name




