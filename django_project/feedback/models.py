import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Feedback(models.Model):
    message = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.message