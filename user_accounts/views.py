from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def home(request):
    return render(request, 'user_accounts/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('user_dashboard')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'user_accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('logout_success')

def admin_logout_view(request):
    logout(request)
    messages.success(request, 'Admin has been logged out successfully.')
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'user_accounts/logout_success.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_accounts/user_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'user_accounts/admin_dashboard.html')
