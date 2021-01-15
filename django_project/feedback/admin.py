"""
    module created automatically
    when the following django command is run
    python manage.py startapp accounts
"""

from django.contrib import admin
from feedback.models import Feedback

# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """ Feedback model and fields """
    list_display = ('author', 'active', 'created', 'updated', 'message')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('message', )
