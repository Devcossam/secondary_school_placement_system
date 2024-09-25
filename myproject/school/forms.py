from django import forms
from .models import School
from django.contrib.auth.models import User

class SchoolSignupForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = School
        fields = ['username','name','email','location','province','contact_number','student_capacity'] 

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        school = super().save(commit=False)
        school.user = user
        if commit:
            school.save()
        return school




class SchoolSearchForm(forms.Form):
    query = forms.CharField(label='Search for a school', max_length=100)


# class SchoolSearchForm(forms.Form):
#     query = forms.CharField(label='Search Schools', required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'Search by school name...',
#         'class': 'search-input'
#     }))