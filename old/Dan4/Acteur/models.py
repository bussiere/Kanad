from django.db import models
from Tag.models import Tag
# Create your models here.


class Acteur(models.Model):
    Pseudo =  models.CharField(max_length=256, null=True, blank=True)
    Tag =  models.ManyToManyField('Tag.Tag')