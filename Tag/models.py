from django.db import models

# Create your models here.


class Tag(models.Model):
    Nom = models.CharField(max_length=256)