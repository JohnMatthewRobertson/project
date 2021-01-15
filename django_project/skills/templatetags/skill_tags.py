""" custom tags for use in templates """

from django import template
from django.db.models import Count
from skills.models import SkillMain, UserSkill, SkillCategory, SkillSubCategory


register = template.Library()


@register.simple_tag(name='skill_type_count_tag')
def total_skill_types():
    """ total number of skills  """
    return SkillMain.publishedSkill.count()


@register.simple_tag()
def all_skill_types():
    """ all skill types fields """
    return SkillMain.publishedSkill.all().values()


@register.simple_tag(name='skill_cat_type_count_tag')
def total_skill_cat_types():
    """ total number of skill category """
    return SkillCategory.publishedSkillCategory.count()


@register.simple_tag()
def all_skill_cat_types():
    """ all skill category fields """
    return SkillCategory.publishedSkillCategory.all().values()


@register.simple_tag(name='skill_sub_type_count_tag')
def total_skill_sub_types():
    """ total number skill sub category """
    return SkillSubCategory.publishedSkillSub.count()


@register.simple_tag()
def all_skill_sub_cat_types():
    """ all skill sub category fields """
    return SkillSubCategory.publishedSkillSub.all().values()


@register.simple_tag()
def total_skill_freq_types(count=5):
    """ return top 5 skills associated with users """
    return UserSkill.publishedUserSkill.all().values('user_skill', 'user_skill__skill_name').annotate(count_total=Count('user_skill')).order_by('-count_total')[:count]


@register.simple_tag()
def total_skill_cat_freq_types(count=5):
    """ return top 5 skills category associated with users """
    return UserSkill.publishedUserSkill.all().values('user_skill_category', 'user_skill_category__skill_category').annotate(count_total=Count('user_skill_category')).order_by('-count_total')[:count]


@register.simple_tag()
def total_skill_sub_freq_types(count=5):
    """ return top 5 skills sub category associated with users """
    return UserSkill.publishedUserSkill.all().values('user_skill_sub_category', 'user_skill_sub_category__skill_sub_category').annotate(count_total=Count('user_skill_sub_category')).order_by('-count_total')[:count]


@register.simple_tag()
def total_users():
    """ number of users with skills  """
    return UserSkill.publishedUserSkill.values('author_id').distinct().count()
