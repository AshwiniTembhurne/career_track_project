from django.contrib import admin
from .models import ContactMessage

# Registering the ContactMessage model to the admin panel
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns to display in the admin list view
    search_fields = ('name', 'email')  # Allows the admin to search messages by name and email
    list_filter = ('created_at',)  # Adds a filter by creation date
