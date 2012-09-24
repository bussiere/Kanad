from django.db import models
from Acteur.models import Acteur
from Tag.models import Tag
# Create your models here.


class Film(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Description_courte = models.TextField(max_length=1204, null=True, blank=True)
    Description_Longue =models.TextField(max_length=2048, null=True, blank=True) 
    Acteurs =  models.ManyToManyField('Acteur.Acteur')
    Cout_Tickets = models.IntegerField()
    Tag = models.ManyToManyField('Tag.Tag')
    Id_daily = models.IntegerField()
    Date = models.DateField()
    Ordre = models.IntegerField()