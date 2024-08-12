# Generated by Django 4.2.14 on 2024-08-09 17:33

from django.db import migrations, models
import user_accounts.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[user_accounts.models.validate_username]),
        ),
    ]