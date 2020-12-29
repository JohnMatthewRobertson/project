from django.contrib import admin
from .models import Feedback

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('author', 'active', 'created', 'updated', 'message')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('message',)
