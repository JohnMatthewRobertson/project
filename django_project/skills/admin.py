from django.contrib import admin
from skills.models import Skill

# Register your models here.

class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_description",)


admin.site.register(Skill, SkillAdmin)
