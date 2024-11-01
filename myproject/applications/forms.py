from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name', 'school', 'age', 'gender', 'student_phone', 'student_email',
            'address', 'province', 'grade_level', 'last_school',
            'last_school_address', 'parent_name', 'parent_phone',
            'appload_results', 'health_history'
        ]
        widgets = {
            'gender': forms.RadioSelect,  # Display gender as radio buttons
        }

class ApplicationCheckForm(forms.Form):
    application_id = forms.IntegerField(label='Application ID')
