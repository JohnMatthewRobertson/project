""" custom tags for use in tempates """

from django import template
from feedback.models import Feedback


register = template.Library()


@register.simple_tag(name='feedback_message_count_tag')
def total_feedback_messsages():
    """ count total number of feedback messages """
    return Feedback.publishedFeedback.count()
