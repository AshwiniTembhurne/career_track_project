from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    application_date = forms.DateField(

        widget=forms.DateInput(attrs={'type': 'date'}),  # HTML5 date input

        input_formats=['%Y-%m-%d']  # Expected input format

    )
    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_title', 'application_date', 'status', 'notes']
