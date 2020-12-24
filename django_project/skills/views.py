from django.shortcuts import render
from django.views.generic import ListView, DetailView
from skills.models import Skill

# Create your views here.

class SkillListView(ListView):
    model = Skill
    context_object_name = 'skill_list'
    template_name = 'skills/skill_list.html'

class SkillDetailView(DetailView):
    model = Skill
    context_object_name = 'skill'
    template_name = 'skills/skill_detail.html'
