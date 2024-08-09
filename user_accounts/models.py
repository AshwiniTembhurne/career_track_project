from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Validator to allow only one space in the username
def validate_username(value):
    # Count spaces and ensure there's only one
    if value.count(' ') > 1:
        raise ValidationError(
            _('Username can contain only one space.'),
            params={'value': value},
        )
    # Ensure the username doesn't start or end with a space
    if value.startswith(' ') or value.endswith(' '):
        raise ValidationError(
            _('Username cannot start or end with a space.'),
            params={'value': value},
        )

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # Apply the custom validator to the username field
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[validate_username],  # Add the custom validator here
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
