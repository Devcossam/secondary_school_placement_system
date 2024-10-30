from django import forms
from .models import School,Rating
from django.contrib.auth.models import User

class SchoolSignupForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = School
        fields = ['username','name','email','location','province','contact_number',
                  'grade_12_capacity','grade_11_capacity','grade_10_capacity',
                  'grade_9_capacity','grade_8_capacity'] 

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
    
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'score': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),
        }


class SchoolSearchForm(forms.Form):
    query = forms.CharField(label='Search for a school', max_length=100)


# class SchoolSearchForm(forms.Form):
#     query = forms.CharField(label='Search Schools', required=False, widget=forms.TextInput(attrs={
#         'placeholder': 'Search by school name...',
#         'class': 'search-input'
#     }))