from django import forms
from django.contrib.auth.models import User
from .models import Pupil

class PupilSignupForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    class Meta:
        model = Pupil
        fields = ['username','name','email','contact','grade','home_address'] 

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        pupil = super().save(commit=False)
        pupil.user = user
        if commit:
            pupil.save()
        return pupil

# from django import forms
# from .models import Pupil

# class PupilSignupForm(forms.ModelForm):
#     class Meta:
#         model = Pupil 
#         fields = [
#             'name','email','contact',
#             'grade','home_address',
#         ]
