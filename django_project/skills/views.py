from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from skills.models import Skill

# Create your views here.

class SkillListView(LoginRequiredMixin, ListView):
    model = Skill
    context_object_name = 'skill_list'
    template_name = 'skills/skill_list.html'
    login_url = 'account_login'

class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    context_object_name = 'skill'
    template_name = 'skills/skill_detail.html'
    login_url = 'account_login'

class SearchResultsListView(ListView):
    model = Skill
    context_object_name = 'skill_list'
    template_name = 'skills/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Skill.objects.filter(
            Q(skill_name__icontains=query) | Q(skill_category__skill_category__icontains=query))