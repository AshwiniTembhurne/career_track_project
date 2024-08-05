from django.shortcuts import render, redirect
from django.contrib import messages

def about_us(request):
    return render(request, 'pages/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        # Process form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Normally, you would send this data to your email or save it in your database.
        # For simplicity, we're just printing it to the console (you can replace this with your logic).
        print(f"Contact Form Submitted: {name}, {email}, {message}")
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')  # Redirect to the same page after submission
    
    # Ensure a response is returned for GET requests
    return render(request, 'pages/contact_us.html')