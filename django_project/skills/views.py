""" better comments """

from django.views import View
from django.urls import reverse_lazy
from django.db.models import Q, Count
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from skills.models import UserSkill, SkillMain, SkillCategory, SkillSubCategory
from skills.forms import (SkillCategoryModelForm,
                          SkillSubCategoryModelForm,
                          SkillMainModelForm,
                          UserSkillModelFormModal,
                          UserSkillCreateModelForm,
                          UserSkillAuthorModelForm)


# Create your views here.


class SkillListView(LoginRequiredMixin, ListView):
    """ better comments """
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/skill_list.html'
    login_url = 'account_login'
    paginate_by = 10


class SearchResultsListView(ListView):
    """ better comments """
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/search_results.html'
    paginate_by = 10

    def get_queryset(self):
        """ better comments """

        result_list = []

        query = self.request.GET.get('q')

        skill = UserSkill.objects.filter(
            Q(user_skill__skill_name__icontains=query))
        if skill:
            skill_query = Q(user_skill__skill_name__icontains=query)
            result_list.append(skill_query)

        category = UserSkill.objects.filter(
            Q(user_skill_category__skill_category__icontains=query))

        if category:
            category_query = Q(
                user_skill_category__skill_category__icontains=query)
            result_list.append(category_query)

        subcat = UserSkill.objects.filter(
            Q(user_skill_sub_category__skill_sub_category__icontains=query))

        if subcat:
            sub_query = Q(
                user_skill_sub_category__skill_sub_category__icontains=query)
            result_list.append(sub_query)

        if len(result_list) == 1:
            return UserSkill.objects.filter(result_list[0]).distinct()
        elif len(result_list) == 2:
            return UserSkill.objects.filter(result_list[0] | result_list[1]).distinct()
        elif len(result_list) == 3:
            return UserSkill.objects.filter(result_list[0] | result_list[1] | result_list[2]).distinct()
        else:
            return UserSkill.objects.none()


class SkillCreateView(BSModalCreateView):
    """ better comments """
    template_name = 'skills/skill_create_skill.html'
    form_class = SkillMainModelForm
    success_message = 'Success: category created'
    success_url = reverse_lazy('skills:user_skill_add')


class SkillCategoryCreateView(BSModalCreateView):
    """ better comments """
    template_name = 'skills/skill_create_skill_category.html'
    form_class = SkillCategoryModelForm
    success_message = 'Success: category created'
    success_url = reverse_lazy('skills:user_skill_add')


class SkillSubCategoryCreateView(BSModalCreateView):
    """ better comments """
    template_name = 'skills/skill_create_skill_sub_category.html'
    form_class = SkillSubCategoryModelForm
    success_message = 'Success: sub category created'
    success_url = reverse_lazy('skills:user_skill_add')


class UserSkillCreate(LoginRequiredMixin, CreateView):
    """ better comments """
    form_class = UserSkillCreateModelForm
    template_name = 'skills/skill_create_user_skill.html'
    login_url = 'account_login'
    success_url = reverse_lazy('skills:user_skill_list')

    def get_form_kwargs(self):
        """ better comments """
        kwargs = super(UserSkillCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """ better comments """
        form.instance.author = self.request.user
        return super(UserSkillCreate, self).form_valid(form)


class UserSkillListView(LoginRequiredMixin, ListView):
    """ better comments """
    model = UserSkill
    context_object_name = 'user_skill_list'
    template_name = 'skills/user_skill_list.html'
    login_url = 'account_login'
    paginate_by = 3

    def get_queryset(self):
        """ better comments """
        return UserSkill.publishedUserSkill.filter(author=self.request.user)

class SkillDetailView(LoginRequiredMixin, ListView):
    """ better comments """
    model = SkillMain
    context_object_name = 'skill_detail_list'
    template_name = 'skills/skill_detail.html'
    login_url = 'account_login'


class SkillCategoryDetailView(LoginRequiredMixin, ListView):
    """ better comments """
    model = SkillCategory
    context_object_name = 'skill_category_detail_list'
    template_name = 'skills/skill_category_detail.html'
    login_url = 'account_login'

class SkillSubCategoryDetailView(LoginRequiredMixin, ListView):
    """ better comments """
    model = SkillSubCategory
    context_object_name = 'skill_sub_category_detail_list'
    template_name = 'skills/skill_sub_category_detail.html'
    login_url = 'account_login'


class SkillDetailUpdateView(BSModalUpdateView):
    """ better comments """
    model = SkillMain
    template_name = 'skills/skill_create_skill.html'
    form_class = SkillMainModelForm
    success_message = 'Success: skill update'
    success_url = reverse_lazy('skills:skill_detail')


class  SkillCategoryDetailUpdateView(BSModalUpdateView):
    """ better comments """
    model = SkillCategory
    template_name = 'skills/skill_create_skill_category.html'
    form_class = SkillCategoryModelForm
    success_message = 'Success: category update'
    success_url = reverse_lazy('skills:skill_category_detail')


class  SkillSubCategoryDetailUpdateView(BSModalUpdateView):
    """ better comments """
    model = SkillSubCategory
    template_name = 'skills/skill_create_skill_sub_category.html'
    form_class = SkillSubCategoryModelForm
    success_message = 'Success: sub category update'
    success_url = reverse_lazy('skills:skill_sub_category_detail')


class UserSkillUpdateView(BSModalUpdateView):
    """ better comments """
    model = UserSkill
    template_name = 'skills/skill_update_skill.html'
    form_class = UserSkillModelFormModal
    success_message = 'Success: category update'
    success_url = reverse_lazy('skills:user_skill_list')


class UserSkillDeleteView(BSModalDeleteView):
    """ better comments """
    model = UserSkill
    context_object_name = 'user'
    template_name = 'skills/skill_delete_skill.html'
    success_message = 'Success: Deleted'
    success_url = reverse_lazy('skills:user_skill_list')


class TeamSkillView(LoginRequiredMixin, View):
    """ better comments """
    model = UserSkill
    login_url = 'account_login'
    context_object_name = 'user_skill_list'
    template_name = 'skills/team_skill.html'

    def get(self, request, *args, **kwargs):
        """ better comments """
        form = UserSkillAuthorModelForm()
        return render(request, self.template_name, {'form': form})


class TeamSearchResultsListView(View):
    """ better comments """

    context_object_name = 'user_skill_list'

    def get(self, request):
        """ better comments """

        data = self.request.GET.getlist('team')

        query_results = UserSkill.objects.filter(author_id__in=data)

        labels = []
        data = []

        pie_chart = query_results.values('user_skill', 'user_skill__skill_name').annotate(
            count_total=Count('user_skill')).order_by('-count_total')

        for item in pie_chart:
            labels.append(item['user_skill__skill_name'])
            data.append(item['count_total'])

        cat_labels = []
        cat_data = []
        cat_chart = query_results.values('user_skill_category', 'user_skill_category__skill_category').annotate(
            count_total=Count('user_skill_category')).order_by('-count_total')

        for item in cat_chart:
            cat_labels.append(item['user_skill_category__skill_category'])
            cat_data.append(item['count_total'])

        sub_labels = []
        sub_data = []
        sub_chart = query_results.values('user_skill_sub_category', 'user_skill_sub_category__skill_sub_category').annotate(
            count_total=Count('user_skill_sub_category')).order_by('-count_total')

        for item in sub_chart:

            sub_labels.append(
                item['user_skill_sub_category__skill_sub_category'])

            sub_data.append(item['count_total'])

        team_count = query_results.values('author_id').distinct().count()

        return render(request,
                      'skills/team_search_results.html',
                      {'labels': labels,
                       'data': data,
                       'catlabels': cat_labels,
                       'catdata': cat_data,
                       'sub_labels': sub_labels,
                       'sub_data': sub_data,
                       'q': query_results,
                       'skilltable': pie_chart,
                       'skillCattable': cat_chart,
                       'skillSubCattable': sub_chart,
                       'teamCount': team_count})
