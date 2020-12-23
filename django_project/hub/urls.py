from django.urls import path
from . import views

app_name = 'hub'

urlpatterns = [
    path('', views.HubHome.as_view(), name='hub_home'),
]