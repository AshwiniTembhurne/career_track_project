from django import forms
from .models import ContactMessage

# This form is tied to the ContactMessage model and will be used in the contact view
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # Fields to display in the form
