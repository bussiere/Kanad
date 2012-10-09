from django.db import models

# Create your models here.

    
    
class Template(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Note = models.TextField(max_length=1024, null=True, blank=True)
    Contenu = models.TextField(max_length=10240, null=True, blank=True)
    def __unicode__(self):
        return self.Nom
    
    
class Page(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)
    Note = models.TextField(max_length=1024, null=True, blank=True)
    Template = models.ManyToManyField('Template', null=True, blank=True)
    def __unicode__(self):
        return self.Nom