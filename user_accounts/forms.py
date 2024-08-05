from django import forms
from django.core.validators import RegexValidator
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
        ],
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

        return cleaned_data
