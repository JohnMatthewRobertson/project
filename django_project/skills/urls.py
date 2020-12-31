from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    #path('', views.SkillListView.as_view(), name='skill_list'),
    path('<uuid:pk>', views.SkillDetailView.as_view(), name='skill_detail'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    #path('add/', views.SkillCreate.as_view(), name='skill_add'),
    path('create/', views.SkillCategoryCreateView.as_view(), name='skill_category_add'),
    path('create_sub/', views.SkillSubCategoryCreateView.as_view(), name='skill_sub_category_add'),
    path('create_skill/', views.SkillCreateView.as_view(), name='skill_add'),
    path('user_skill_add/', views.UserSkillCreate.as_view(), name='user_skill_add'),
    path('', views.UserSkillListView.as_view(), name='user_skill_list'),
    path('update/<uuid:pk>', views.UserSkillUpdateView.as_view(), name='update'),
    path('delete/<uuid:pk>', views.UserSkillDeleteView.as_view(), name='delete'),
]