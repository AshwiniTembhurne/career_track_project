from django.contrib import admin
from job_application.models import JobApplication

# Register your models here.
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'status', 'application_date')
    list_filter = ('status', 'application_date')
    search_fields = ('job_title', 'company_name')

# Register any other models you have
