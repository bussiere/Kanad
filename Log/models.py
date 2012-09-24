from django.db import models
from Engine.models import Page,Template 

# Create your models here.


class Log_Film_Client(models.Model):
    Client =  models.OneToOneField('Client.Client')
    Films = models.OneToOneField('Film.Film')
    Date = models.DateField()
    
class Log_Page_Client(models.Model):
    Client =  models.OneToOneField('Client.Client')
    Page = models.OneToOneField('Engine.Page')
    Date = models.DateField()
    
class Log_Page_Visite(models.Model):
    Ip = models.IPAddressField()
    Page = models.OneToOneField('Engine.Page')
    Date = models.DateField()
    