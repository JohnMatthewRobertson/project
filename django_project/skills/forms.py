from django import forms
from .models import Skill, SkillCategory, SkillSubCategory, SkillMain, UserSkill
from bootstrap_modal_forms.forms import BSModalModelForm


class SkillCategoryModelForm(BSModalModelForm):
    
    class Meta:
        model = SkillCategory
        fields = ['skill_category', 'skill_category_description']

class SkillSubCategoryModelForm(BSModalModelForm):

    class Meta:
        model = SkillSubCategory
        fields = ['skill_sub_category', 'skill_sub_category_description']


class UserSkillModelForm(forms.models.ModelForm):

    class Meta:
        model = UserSkill
        fields = ['user_skill', 'user_skill_category', 'user_skill_sub_category',]

