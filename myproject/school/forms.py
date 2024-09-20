from django import forms

class SchoolSearchForm(forms.Form):
    query = forms.CharField(label='Search for a school', max_length=100)