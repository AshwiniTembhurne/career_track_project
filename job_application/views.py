from django.shortcuts import render, get_object_or_404, redirect
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
            return redirect('home')
    else:
        form = JobApplicationForm()
    return render(request, 'job_application/application_form.html', {'form': form})

def edit_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_details', id=id)
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'job_application/application_form.html', {'form': form})

def delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id)
    if request.method == 'POST':
        application.delete()
        return redirect('home')
    return render(request, 'job_application/confirm_delete.html', {'application': application})
