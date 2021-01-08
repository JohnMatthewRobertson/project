""" url call the class within view """

from django.urls import reverse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from feedback.models import Feedback
from feedback.forms import FeedbackForm


# Create your views here.


class FeedBackList(LoginRequiredMixin, FormMixin, ListView):
    """ feedbacl list and form entry """
    queryset = Feedback.publishedFeedback.all()
    context_object_name = 'feedback_list'
    template_name = 'feedback/feedback_list.html'
    login_url = 'account_login'
    paginate_by = 3
    form_class = FeedbackForm


class NewFeedBack(LoginRequiredMixin, View):
    """ processing new feedback form """

    def post(self, request, *args, **kwargs):
        """ handling form submitted """
        new_feedback = FeedbackForm(request.POST)
        new_feedback.instance.author = request.user

        if new_feedback.is_valid():
            new_feedback.save()
            return redirect(reverse('feedback:feedback_list'))
