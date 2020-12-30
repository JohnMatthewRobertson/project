from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from skills.models import Skill, SkillCategory, SkillSubCategory, UserSkill, SkillMain
from skills.forms import SkillCategoryModelForm, SkillSubCategoryModelForm, SkillMainModelForm, UserSkillModelForm, UserSkillModelFormModal
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView

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

class SkillCreateView(BSModalCreateView):
    template_name = 'skills/skill_create_skill.html'
    form_class = SkillMainModelForm
    success_message = 'Success: category created'
    success_url = reverse_lazy('skills:user_skill_add')
    

class SkillCategoryCreateView(BSModalCreateView):
    template_name = 'skills/skill_create_skill_category.html'
    form_class = SkillCategoryModelForm
    success_message = 'Success: category created'
    success_url = reverse_lazy('skills:user_skill_add')

class SkillSubCategoryCreateView(BSModalCreateView):
    template_name = 'skills/skill_create_skill_sub_category.html'
    form_class = SkillSubCategoryModelForm
    success_message = 'Success: sub category created'
    success_url = reverse_lazy('skills:user_skill_add')

class UserSkillCreate(CreateView):
    model = UserSkill
    fields = ['author', 'user_skill', 'user_skill_category', 'user_skill_sub_category']
    template_name = 'skills/skill_create_user_skill.html'

class UserSkillListView(LoginRequiredMixin, ListView):
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/user_skill_list.html'
    login_url = 'account_login'
    paginate_by = 3

class UserSkillUpdateView(BSModalUpdateView):
    model = UserSkill
    template_name = 'skills/skill_update_skill.html'
    form_class = UserSkillModelFormModal
    success_message = 'Success: category update'
    success_url = reverse_lazy('skills:user_skill_list')