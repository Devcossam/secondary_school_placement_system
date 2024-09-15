from django.db import models

# Create your models here.
class Pupil(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=15,null=True)
    date_joined = models.DateTimeField(auto_now=True,null=True,blank=True)
    grade = models.CharField(max_length=30,null=True)
    home_address = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return f"{self.name}"

