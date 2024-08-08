from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from job_application.models import JobApplication
from job_application.forms import JobApplicationForm

def admin_dashboard(request):
    applications = JobApplication.objects.all()
    paginator = Paginator(applications, 10)  # Show 10 applications per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/admin_dashboard.html', {'page_obj': page_obj})

def admin_application_details(request, id):
    application = get_object_or_404(JobApplication, id=id)
    return render(request, 'admin_panel/application_details.html', {'application': application})

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

def admin_delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Job application deleted successfully!')
        return redirect('admin_dashboard')
    return render(request, 'admin_panel/confirm_delete.html', {'application': application})
