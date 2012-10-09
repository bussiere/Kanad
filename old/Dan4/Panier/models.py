from django.db import models

# Create your models here.

class Panier(models.Model):
    Film = models.ManyToManyField('Film.Film')
    Client = models.ManyToManyField('Client.Client')
    Date = models.DateField()