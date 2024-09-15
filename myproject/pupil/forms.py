from django import forms
from .models import Pupil

class PupilSignupForm(forms.ModelForm):
    class Meta:
        model = Pupil 
        fields = [
            'name','email','contact',
            'grade','home_address',
        ]
