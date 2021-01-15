""" better comments """

from django.views import View
from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from skills.models import UserSkill

# Create your views here.


class HubHome(LoginRequiredMixin, View):
    """ better comments"""
    login_url = 'account_login'

    def get(self, request):
        """ better comments """
        labels = []
        data = []
        pie_chart = UserSkill.publishedUserSkill.all().values('user_skill', 'user_skill__skill_name').annotate(
            count_total=Count('user_skill')).order_by('-count_total')[:5]

        for item in pie_chart:
            labels.append(item['user_skill__skill_name'])
            data.append(item['count_total'])

        cat_labels = []
        cat_data = []
        cat_chart = UserSkill.publishedUserSkill.all().values('user_skill_category', 'user_skill_category__skill_category').annotate(
            count_total=Count('user_skill_category')).order_by('-count_total')[:5]

        for item in cat_chart:
            cat_labels.append(item['user_skill_category__skill_category'])
            cat_data.append(item['count_total'])

        sub_labels = []
        sub_data = []
        sub_chart = UserSkill.publishedUserSkill.all().values('user_skill_sub_category', 'user_skill_sub_category__skill_sub_category').annotate(
            count_total=Count('user_skill_sub_category')).order_by('-count_total')[:5]

        for item in sub_chart:
            sub_labels.append(
                item['user_skill_sub_category__skill_sub_category'])
            sub_data.append(item['count_total'])

        return render(request,
                      'hub/home.html',
                      {'labels': labels,
                       'data': data,
                       'catlabels': cat_labels,
                       'catdata': cat_data,
                       'subdata': sub_data,
                       'sublabels': sub_labels, })
