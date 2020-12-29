from django import template
from feedback.models import Feedback
from django.db.models import Count
from django.utils.safestring import mark_safe

register = template.Library()
@register.simple_tag(name='feedback_message_count_tag')
def total_feedback_messsages():
    return Feedback.publishedFeedback.count()