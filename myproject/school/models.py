from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    province = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    grade_12_capacity = models.PositiveIntegerField(default=0)
    grade_12_enrollment = models.PositiveIntegerField(default=0)

    grade_11_capacity = models.PositiveIntegerField(default=0)
    grade_11_enrollment = models.PositiveIntegerField(default=0)

    grade_10_capacity = models.PositiveIntegerField(default=0)
    grade_10_enrollment = models.PositiveIntegerField(default=0)

    grade_9_capacity = models.PositiveIntegerField(default=0)
    grade_9_enrollment = models.PositiveIntegerField(default=0)

    grade_8_capacity = models.PositiveIntegerField(default=0)
    grade_8_enrollment = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.name

    def school_capacity(self):
        return (
            self.grade_12_capacity + self.grade_11_capacity + self.grade_10_capacity + 
            self.grade_9_capacity + self.grade_8_capacity 
        )
    
    def available_space_grade_12(self):
        return self.grade_12_capacity - self.grade_12_enrollment

    def available_space_grade_11(self):
        return self.grade_11_capacity - self.grade_11_enrollment

    def available_space_grade_10(self):
        return self.grade_10_capacity - self.grade_10_enrollment

    def available_space_grade_9(self):
        return self.grade_9_capacity - self.grade_9_enrollment

    def available_space_grade_8(self):
        return self.grade_8_capacity - self.grade_8_enrollment
    
    def total_enrollment(self):
        return (self.grade_12_enrollment + self.grade_11_enrollment + 
                                        self.grade_10_enrollment + 
                                        self.grade_9_enrollment + 
                                        self.grade_8_enrollment)

    
    # def total_available_space(self):
    #     return self.total_capacity() - self.total_enrollment()
    def total_available_space(self):
        capacity = self.school_capacity()
        enrollment = self.total_enrollment()
        available_space = capacity - enrollment
        return max(available_space, 0)  # Ensure we don't return negative values




    






