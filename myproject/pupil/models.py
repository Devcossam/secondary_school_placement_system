from django.db import models

# Create your models here.
class Pupil(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"