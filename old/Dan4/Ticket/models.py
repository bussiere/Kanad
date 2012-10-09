from django.db import models

# Create your models here.


class PackTicket(models.Model):
    Prix = models.FloatField()
    Nbre = models.IntegerField()

    