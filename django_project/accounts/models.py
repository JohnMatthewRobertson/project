"""
    module created automatically
    when the following django command is run
    python manage.py startapp accounts
"""

from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    """ place holder class for custom user """
    pass
