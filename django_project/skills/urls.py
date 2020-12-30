from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.SkillListView.as_view(), name='skill_list'),
    path('<uuid:pk>', views.SkillDetailView.as_view(), name='skill_detail'),
    path('search/', views.SearchResultsListView.as_view(), name='search_results'),
    path('add/', views.SkillCreate.as_view(), name='skill_add'),
    path('create/', views.SkillCategoryCreateView.as_view(), name='skill_category_add'),
    path('create_sub/', views.SkillSubCategoryCreateView.as_view(), name='skill_sub_category_add'),
 
]