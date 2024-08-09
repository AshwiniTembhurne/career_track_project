from django.db import models

# This model will store the contact form messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)  # The name of the user
    email = models.EmailField()  # The user's email
    message = models.TextField()  # The message content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the message was created

    def __str__(self):
        return f'Message from {self.name} ({self.email})'

