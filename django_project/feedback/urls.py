""" url endpoints """

from django.urls import path
from feedback.views import FeedBackList, NewFeedBack

app_name = 'feedback'

urlpatterns = [
    path('', FeedBackList.as_view(), name='feedback_list'),
    path('new', NewFeedBack.as_view(), name='new_feedback'),
]
