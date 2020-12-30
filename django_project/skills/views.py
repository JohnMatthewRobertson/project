from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from skills.models import Skill, SkillCategory, SkillSubCategory
from skills.forms import SkillCategoryModelForm, SkillSubCategoryModelForm
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView

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

class SkillCreate(CreateView):
    model = Skill
    fields = ['skill_name', 'skill_description', 'skill_category', 'skill_sub_category']


class SkillCategoryCreateView(BSModalCreateView):
    template_name = 'skills/skill_create_skill_category.html'
    form_class = SkillCategoryModelForm
    success_message = 'Success: category created'
    success_url = reverse_lazy('skills:skill_add')

class SkillSubCategoryCreateView(BSModalCreateView):
    template_name = 'skills/skill_create_skill_sub_category.html'
    form_class = SkillSubCategoryModelForm
    success_message = 'Success: sub category created'
    success_url = reverse_lazy('skills:skill_add')