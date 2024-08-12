from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from job_application.models import JobApplication
from job_application.forms import JobApplicationForm
from user_accounts.models import CustomUser
from user_accounts.forms import UserRegistrationForm  # Assuming this form can be used to edit users

# Admin dashboard view with pagination for job applications
@login_required
def admin_dashboard(request):
    applications = JobApplication.objects.all()
    paginator = Paginator(applications, 10)  # Show 10 applications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/admin_dashboard.html', {'page_obj': page_obj})

# Detailed view of a specific job application
@login_required
def admin_application_details(request, id):
    application = get_object_or_404(JobApplication, id=id)
    return render(request, 'admin_panel/application_details.html', {'application': application})

# View to add a new job application
@login_required
def admin_add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application added successfully!')
            return redirect('admin_dashboard')
    else:
        form = JobApplicationForm()
    return render(request, 'admin_panel/application_form.html', {'form': form})

# View to edit an existing job application
@login_required
def admin_edit_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'admin_panel/application_form.html', {'form': form})

# View to delete a job application
@login_required
def admin_delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Job application deleted successfully!')
        return redirect('admin_dashboard')
    return render(request, 'admin_panel/confirm_delete.html', {'application': application})

# View to list all users with pagination
@login_required
def user_list(request):
    if not request.user.is_superuser:
        return redirect('login')  # Only superusers can access this view
    users = CustomUser.objects.all()
    paginator = Paginator(users, 10)  # Show 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/user_list.html', {'page_obj': page_obj})

# View to edit a specific user
@login_required
def user_edit(request, user_id):
    if not request.user.is_superuser:
        return redirect('login')  # Only superusers can access this view
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('user_list')
    else:
        form = UserRegistrationForm(instance=user)
    return render(request, 'admin_panel/user_edit.html', {'form': form, 'user': user})

# View to confirm deletion of a user
@login_required
def user_delete(request, user_id):
    if not request.user.is_superuser:
        return redirect('login')  # Only superusers can access this view
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('user_list')
    return render(request, 'admin_panel/user_confirm_delete.html', {'user': user})
