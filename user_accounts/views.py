from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import UserRegistrationForm
from job_application.models import JobApplication

def home(request):
    return render(request, 'user_accounts/home.html')
    
# Added success message and redirect to signup_success after successful sign-up.
def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('signup_success')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'user_accounts/signup.html', {'form': form})

# View for successful sign-up page
def signup_success(request):
    return render(request, 'user_accounts/signup_success.html')

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
    return redirect('logout_success')

def admin_logout_view(request):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'user_accounts/logout_success.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_accounts/user_dashboard.html')

@login_required
def admin_dashboard(request):
    applications = JobApplication.objects.all()
    paginator = Paginator(applications, 10)  # Show 10 applications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/admin_dashboard.html', {'page_obj': page_obj})
