from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.SkillListView.as_view(), name='skill_list'),
    path('<uuid:pk>', views.SkillDetailView.as_view(), name='skill_detail'),
]