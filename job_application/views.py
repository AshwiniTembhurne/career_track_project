from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import JobApplication
from .forms import JobApplicationForm

@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    paginator = Paginator(applications, 10)  # Show 10 applications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'job_application/application_list.html', {'page_obj': page_obj})

@login_required
def application_details(request, id):
    application = get_object_or_404(JobApplication, id=id, user=request.user)
    return render(request, 'job_application/application_details.html', {'application': application})

@login_required
def add_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.user = request.user
            new_application.save()
            messages.success(request, 'Job application added successfully!')
            return redirect('application_details', id=new_application.id)
    else:
        form = JobApplicationForm()
    return render(request, 'job_application/application_form.html', {'form': form})

@login_required
def edit_application(request, id):
    application = get_object_or_404(JobApplication, id=id, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application updated successfully!')
            return redirect('application_details', id=id)
    else:
        form = JobApplicationForm(instance=application)
    return render(request, 'job_application/application_form.html', {'form': form})

@login_required
def delete_application(request, id):
    application = get_object_or_404(JobApplication, id=id, user=request.user)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Job application deleted successfully!')
        return redirect('application_list')
    return render(request, 'job_application/confirm_delete.html', {'application': application})
