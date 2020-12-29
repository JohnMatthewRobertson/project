from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class FeedBackList(LoginRequiredMixin, FormMixin, ListView):
    queryset = Feedback.publishedFeedback.all()
    context_object_name = 'feedback_list'
    template_name = 'feedback/feedback_list.html'
    login_url = 'account_login'
    paginate_by = 3
    form_class = FeedbackForm


class NewFeedBack(LoginRequiredMixin, View):

    def post(self,request, *args, **kwargs):
        new_feedback = FeedbackForm(request.POST
        print(new_feedback['message'])

        if request.user.is_authenticated:
            print("john")
            new_feedback.author = 'admin'

        if new_feedback.is_valid():
            print("john")
            new_feedback.save()
            return redirect('feedback:feedback_list')

