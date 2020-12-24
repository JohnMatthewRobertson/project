from django.contrib import admin
from .models import Feedback

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("message", "author",)

admin.site.register(Feedback, FeedbackAdmin)