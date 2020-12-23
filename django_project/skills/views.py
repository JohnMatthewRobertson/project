from django.shortcuts import render
from django.views.generic import ListView
from skills.models import Skill

# Create your views here.

class SkillListView(ListView):
    print("john")
    model = Skill
    template_name = 'skills/skill_list.html'
