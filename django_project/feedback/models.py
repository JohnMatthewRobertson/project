import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class PublishedFeedbackManager(models.Manager):

    def get_queryset(self):
        return super(PublishedFeedbackManager, self).get_queryset().filter(active=True)

class Feedback(models.Model):

    objects = models.Manager() # default manager
    publishedFeedback = PublishedFeedbackManager() # custom manager

    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='feedback')
    message = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'feedback by {self.author} on {self.message}'