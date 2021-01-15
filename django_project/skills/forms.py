""" forms for skills """

from django import forms
from skills.models import SkillCategory, SkillSubCategory, SkillMain, UserSkill
from bootstrap_modal_forms.forms import BSModalModelForm


class SkillMainModelForm(BSModalModelForm):
    """ skill form used in modal """

    class Meta:
        """ model, fields from model to use """
        model = SkillMain
        fields = ['skill_name', 'skill_description']


class SkillCategoryModelForm(BSModalModelForm):
    """ skill category form used in modal """

    class Meta:
        """ model, fields from model to use """
        model = SkillCategory
        fields = ['skill_category', 'skill_category_description']


class SkillSubCategoryModelForm(BSModalModelForm):
    """ skill sub category form used in modal """

    class Meta:
        """ model, fields from model to use """
        model = SkillSubCategory
        fields = ['skill_sub_category', 'skill_sub_category_description']


class UserSkillModelForm(forms.models.ModelForm):
    """ form used for user skill """

    class Meta:
        """ model, fields from model to use """
        model = UserSkill
        fields = ['user_skill', 'user_skill_category',
                  'user_skill_sub_category', ]


class UserSkillAuthorModelForm(forms.Form):
    """ form used for team skill mix selection """
    names = UserSkill.objects.values_list(
        'author_id', 'author__username').distinct().order_by()
    
    team = forms.MultipleChoiceField(
        choices=names,
        widget=forms.SelectMultiple(),
        required=True,
        label='Team members',
    )


class UserSkillModelFormModal(BSModalModelForm):
    """ form used user skill modal """

    class Meta:
        """ model, fields from model to use """
        model = UserSkill
        fields = ['user_skill',
                  'user_skill_category',
                  'user_skill_sub_category',
                  'active',
                  'teach', ]


class UserSkillCreateModelForm(forms.models.ModelForm):
    """ form used for adding skill to user """

    class Meta:
        """ model, fields from model to use """
        model = UserSkill
        fields = ['user_skill',
                  'user_skill_category',
                  'user_skill_sub_category',
                  'teach', ]

    def __init__(self, *args, **kwargs):
        """ exclude skills already assigned to user """
        user = kwargs.pop('user')
        super(UserSkillCreateModelForm, self).__init__(*args, **kwargs)
        if self.instance:
            user_skill_query_set = UserSkill.objects.filter(
                author=user).values_list('user_skill__skill_name', flat=True)
            self.fields['user_skill'].queryset = SkillMain.objects.exclude(
                skill_name__in=user_skill_query_set)
