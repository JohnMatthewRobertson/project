"""
    module created automatically
    when the following django command is run
    python manage.py startapp accounts
"""

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class PublishedFeedbackManager(models.Manager):
    """ model for feedback """

    def get_queryset(self):
        """ return query set """
        return super(PublishedFeedbackManager, self).get_queryset().filter(active=True)


class Feedback(models.Model):
    """ feedback model """

    objects = models.Manager()  # default manager
    publishedFeedback = PublishedFeedbackManager()  # custom manager

    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='feedback')
    message = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        """ order the model """
        ordering = ('-created',)

    def __str__(self):
        """ return custom string format """
        return f'feedback by {self.author} on {self.message}'
