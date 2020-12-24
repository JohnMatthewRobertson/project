import uuid
from django.db import models
from django.urls import reverse


# Create your models here.

class Skill(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    skill_name = models.CharField(max_length=200)
    skill_description = models.CharField(max_length=300)


    def __str__(self):
        return self.skill_name

    def get_absolute_url(self):
        return reverse('skills:skill_detail', args=[str(self.id)])
