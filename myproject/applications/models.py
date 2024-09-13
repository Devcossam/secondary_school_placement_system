from django.db import models
from school.models import School
from pupil.models import Pupil

class Application(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    # Foreign Key relationships
    pupil = models.ForeignKey(Pupil, null=True, blank=True, on_delete=models.SET_NULL)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)  

    # Application details
    date_applied = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')

    # Pupil Information
    name = models.CharField(max_length=100, blank=True,null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True,null=True)
    student_phone = models.CharField(max_length=15, blank=True,null=True)
    student_email = models.EmailField(blank=True,null=True)
    address = models.CharField(max_length=255, blank=True,null=True)
    province = models.CharField(max_length=100, blank=True,null=True)
    grade_level = models.CharField(max_length=50, blank=True,null=True)
    last_school = models.CharField(max_length=100, blank=True,null=True)
    last_school_address = models.CharField(max_length=255, blank=True,null=True)

    # Parent/Guardian Information
    parent_name = models.CharField(max_length=100, blank=True,null=True)
    parent_phone = models.CharField(max_length=15, blank=True,null=True)

    # File Uploads
    documents = models.FileField(upload_to='documents/', blank=True, null=True)

    # Health History
    health_history = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"Application by {self.name} for {self.school if self.school else 'unspecified school'}"
