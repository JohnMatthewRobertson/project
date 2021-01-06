from django import template
from skills.models import SkillMain, UserSkill, SkillCategory, SkillSubCategory
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model

register = template.Library()
@register.simple_tag(name='skill_type_count_tag')
def total_skill_types():
    return SkillMain.publishedSkill.count()

@register.simple_tag()
def all_skill_types():
    return SkillMain.publishedSkill.all().values()

@register.simple_tag(name='skill_cat_type_count_tag')
def total_skill_cat_types():
    return SkillCategory.publishedSkillCategory.count()

@register.simple_tag()
def all_skill_cat_types():
    return SkillCategory.publishedSkillCategory.all().values()

@register.simple_tag(name='skill_sub_type_count_tag')
def total_skill_sub_types():
    return SkillSubCategory.publishedSkillSub.count()

@register.simple_tag()
def all_skill_sub_cat_types():
    return SkillSubCategory.publishedSkillSub.all().values()


@register.simple_tag()
def total_skill_freq_types(count=5):
    #return UserSkill.publishedUserSkill.all().values_list('user_skill', 'user_skill__skill_name').annotate(
    return UserSkill.publishedUserSkill.all().values('user_skill', 'user_skill__skill_name').annotate(

        count_total = Count('user_skill')
        ).order_by('-count_total')[:count]

@register.simple_tag()
def total_skill_cat_freq_types(count=5):
    #return UserSkill.publishedUserSkill.all().values_list('user_skill', 'user_skill__skill_name').annotate(
    return UserSkill.publishedUserSkill.all().values('user_skill_category', 'user_skill_category__skill_category').annotate(

        count_total = Count('user_skill_category')
        ).order_by('-count_total')[:count]

@register.simple_tag()
def total_skill_sub_freq_types(count=5):
    #return UserSkill.publishedUserSkill.all().values_list('user_skill', 'user_skill__skill_name').annotate(
    return UserSkill.publishedUserSkill.all().values('user_skill_sub_category', 'user_skill_sub_category__skill_sub_category').annotate(

        count_total = Count('user_skill_sub_category')
        ).order_by('-count_total')[:count]

@register.simple_tag()
def total_users():
    return UserSkill.publishedUserSkill.values('author_id').distinct().count()