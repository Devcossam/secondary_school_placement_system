from django import forms
from .models import Pupil

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'date_of_birth', 'address','password']
