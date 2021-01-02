from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from skills.models import SkillCategory, SkillSubCategory, UserSkill, SkillMain
from skills.forms import SkillCategoryModelForm, SkillSubCategoryModelForm, SkillMainModelForm, UserSkillModelForm, UserSkillModelFormModal, UserSkillCreateModelForm
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy, reverse
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView

# Create your views here.

class SkillListView(LoginRequiredMixin, ListView):
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/skill_list.html'
    login_url = 'account_login'
    paginate_by = 10



'''
class SkillDetailView(LoginRequiredMixin, DetailView):
    model = Skill
    context_object_name = 'skill'
    template_name = 'skills/skill_detail.html'
    login_url = 'account_login'
'''

class SearchResultsListView(ListView):
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/search_results.html'

    def get_queryset(self):

        result_list = []

        query = self.request.GET.get('q')

        print(query)

        skill = UserSkill.objects.filter(Q(user_skill__skill_name__icontains=query))
        if skill:
            skill_query = Q(user_skill__skill_name__icontains=query)
            result_list.append(skill_query) 
        print("SKILL", skill)

        category = UserSkill.objects.filter(Q(user_skill_category__skill_category__icontains=query))
        print("CAT", category)
        if category:
            category_query = Q(user_skill_category__skill_category__icontains=query)
            result_list.append(category_query) 

        subcat = UserSkill.objects.filter(Q(user_skill_sub_category__skill_sub_category__icontains=query))
        print("SUB", subcat)
        if subcat:
            sub_query = Q(user_skill_sub_category__skill_sub_category__icontains=query)
            result_list.append(sub_query)

        print("LIST", result_list)

        for item in result_list:
            print(type(item))
            
        print(len(result_list))

        if len(result_list) == 1:
            return UserSkill.objects.filter(result_list[0]).distinct()
        elif len(result_list) == 2:
            return UserSkill.objects.filter(result_list[0] | result_list[1]).distinct()
        elif len(result_list) == 3:
            return UserSkill.objects.filter(result_list[0] | result_list[1] | result_list[2]).distinct()
        else:
            return UserSkill.objects.none()

        #print("TEST", UserSkill.objects.filter(Q(user_skill_category__skill_category__icontains=query) & Q(user_skill_sub_category__skill_sub_category__icontains=query)))

        #return UserSkill.objects.filter(Q(user_skill_category__skill_category__icontains=query) | Q(user_skill_sub_category__skill_sub_category__icontains=query)).distinct()


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

class UserSkillCreate(LoginRequiredMixin, CreateView):
    form_class = UserSkillCreateModelForm
    template_name = 'skills/skill_create_user_skill.html'
    login_url = 'account_login'
    success_url = reverse_lazy('skills:user_skill_list')

    def get_form_kwargs(self):
        kwargs = super(UserSkillCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UserSkillCreate, self).form_valid(form)


class UserSkillListView(LoginRequiredMixin, ListView):
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/user_skill_list.html'
    login_url = 'account_login'
    paginate_by = 3

    def get_queryset(self):
        return UserSkill.publishedUserSkill.filter(author=self.request.user)



class UserSkillUpdateView(BSModalUpdateView):
    model = UserSkill
    template_name = 'skills/skill_update_skill.html'
    form_class = UserSkillModelFormModal
    success_message = 'Success: category update'
    success_url = reverse_lazy('skills:user_skill_list')

class UserSkillDeleteView(BSModalDeleteView):
    model = UserSkill
    context_object_name = 'user'
    template_name = 'skills/skill_delete_skill.html'
    success_message = 'Success: Deleted'
    success_url = reverse_lazy('skills:user_skill_list')
