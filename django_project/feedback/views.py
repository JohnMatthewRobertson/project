from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

class FeedBackList(LoginRequiredMixin, ListView):
    model = Feedback
    context_object_name = 'feedback_list'
    template_name = 'feedback/feedback_list.html'
    login_url = 'account_login'

class NewFeedBack(CreateView):
    model = Feedback
    fields = ['message', 'author',]
    success_url = reverse_lazy('feedback:feedback_list')

        




