""" better comment """

from django.urls import path
from skills.views import (SkillListView,
                          SearchResultsListView,
                          SkillCategoryCreateView,
                          SkillSubCategoryCreateView,
                          SkillCreateView,
                          UserSkillCreate,
                          UserSkillListView,
                          UserSkillUpdateView,
                          UserSkillDeleteView,
                          TeamSkillView,
                          TeamSearchResultsListView)

app_name = 'skills'

urlpatterns = [
    path('skill_list/', SkillListView.as_view(), name='skill_list'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('create/', SkillCategoryCreateView.as_view(), name='skill_category_add'),
    path('create_sub/', SkillSubCategoryCreateView.as_view(),
         name='skill_sub_category_add'),
    path('create_skill/', SkillCreateView.as_view(), name='skill_add'),
    path('user_skill_add/', UserSkillCreate.as_view(), name='user_skill_add'),
    path('', UserSkillListView.as_view(), name='user_skill_list'),
    path('update/<uuid:pk>', UserSkillUpdateView.as_view(), name='update'),
    path('delete/<uuid:pk>', UserSkillDeleteView.as_view(), name='delete'),
    path('team_skill', TeamSkillView.as_view(), name='team_skill'),
    path('team_search/', TeamSearchResultsListView.as_view(),
         name='team_search_results'),
]
