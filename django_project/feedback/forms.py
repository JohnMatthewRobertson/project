""" forms for accounts """

from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.models.ModelForm):
    """ feedback form """
    class Meta:
        """ model, fields """
        model = Feedback
        fields = ['message', ]
