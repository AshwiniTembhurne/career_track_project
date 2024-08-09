# Generated by Django 4.2.14 on 2024-08-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0003_jobapplication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('', 'Select Status'), ('AP', 'Applied'), ('RJ', 'Rejected'), ('IP', 'In Progress'), ('CD', 'Completed'), ('OD', 'Offered')], default='', max_length=2),
        ),
    ]
