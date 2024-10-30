from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum



class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    # admin_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='school', null=True, blank=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    date_joined = models.DateTimeField(auto_now=True,null=True,blank=True)
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

    class Meta:
        db_table = 'school'
    

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

  
    def total_available_space(self):
        capacity = self.school_capacity()
        enrollment = self.total_enrollment()
        available_space = capacity - enrollment
        return max(available_space, 0)  # Ensure we don't return negative values
    

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return sum(rating.score for rating in ratings) / ratings.count()
        return 0
    
    def total_stars(self):
        ratings = self.ratings.all()
        return sum(rating.score for rating in ratings)
    
    @classmethod
    def get_top_rated_schools(cls):
        return (
            cls.objects.annotate(total_stars=Sum('ratings__score'))
            .filter(total_stars__gt=100)
            .order_by('-total_stars')
        )

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='ratings', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)  # Rating score (e.g., 1 to 5)
    comment = models.TextField(blank=True, null=True)  # Optional comment

    class Meta:
        unique_together = ('user', 'school')  # Ensure one rating per user per school

    def __str__(self):
        return f"{self.user.username} - {self.school.name}: {self.score}"



    






