from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.FeedBackList.as_view(), name='feedback_list'),
    path('new', views.NewFeedBack.as_view(), name='new_feedback'),
]