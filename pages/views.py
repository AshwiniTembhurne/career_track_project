from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm  # Import the form

# About Us view remains the same
def about_us(request):
    return render(request, 'pages/about_us.html')

# Updated Contact Us view
def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Bind the form to POST data
        if form.is_valid():  # Validate the form data
            form.save()  # Save the form data to the database
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_us')  # Redirect to the same page after submission
    else:
        form = ContactForm()  # Render an empty form for GET requests
    
    return render(request, 'pages/contact_us.html', {'form': form})  # Pass the form to the template
