from django.contrib import admin
from job_application.models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'status', 'application_date', 'user')
    list_filter = ('status', 'application_date')
    search_fields = ('job_title', 'company_name', 'user__username')
