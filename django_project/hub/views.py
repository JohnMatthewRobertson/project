from django.views.generic import TemplateView

# Create your views here.

class HubHome(TemplateView):
    template_name = 'hub/home.html'