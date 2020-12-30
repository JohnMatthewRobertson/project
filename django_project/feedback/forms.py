from django import forms
from django.core.exceptions import ValidationError
from feedback.models import Feedback

class FeedbackForm(forms.models.ModelForm):

    class Meta:
        model = Feedback
        fields = ['message', ]



        