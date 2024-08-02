from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import JobApplication
from .forms import JobApplicationForm

def application_details(request, id):
    application = get_object_or_404(JobApplication, id=id)
    return render(request, 'job_application/application_details.html', {'application': application})

def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application added successfully!')
            return redirect('application_list')
        else:
            print(form.errors)  # Debugging output
    else:
        form = JobApplicationForm()
    return render(request, 'job_application/application_form.html', {'form': form})

def edit_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application updated successfully!')
            return redirect('application_details', id=id)
        else:
            print(form.errors)  # Debugging output
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'job_application/application_form.html', {'form': form})

def delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Job application deleted successfully!')
        return redirect('application_list')
    return render(request, 'job_application/confirm_delete.html', {'application': application})

def application_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'job_application/application_list.html', {'applications': applications})
