from django.db import models

# Create your models here.


class Client(models.Model):
    Nbre_Tickets = models.IntegerField()
    Date = models.DateField()