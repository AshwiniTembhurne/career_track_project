from django.db import models
from django.conf import settings

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('', 'Select Status'),  # Blank option
        ('AP', 'Applied'),
        ('RJ', 'Rejected'),
        ('IP', 'In Progress'),
        ('CD', 'Completed'),
        ('OD', 'Offered'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    application_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='', blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_title
