"""
    module created automatically
    when the following django command is run
    python manage.py startapp <app name>
"""

from django.urls import path
from hub.views import HubHome

app_name = 'hub'

urlpatterns = [
    path('', HubHome.as_view(), name='hub_home'),
]
