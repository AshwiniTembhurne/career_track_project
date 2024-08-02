from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    application_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = JobApplication
        fields = ['company_name', 'job_title', 'application_date', 'status', 'notes']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'job_title': forms.TextInput(attrs={'placeholder': 'Enter Job Title'}),
            'status': forms.Select(choices=JobApplication.STATUS_CHOICES),  # Use Select widget for dropdown
            'notes': forms.Textarea(attrs={'placeholder': 'Enter any additional notes'}),
        }
