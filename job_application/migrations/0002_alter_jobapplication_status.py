# Generated by Django 4.2.14 on 2024-08-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(blank=True, choices=[('', 'Select Status'), ('AP', 'Applied'), ('RJ', 'Rejected'), ('IP', 'In Progress'), ('CP', 'Completed')], default='', max_length=2),
        ),
    ]
