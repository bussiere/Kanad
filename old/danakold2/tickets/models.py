from django.db import models
# Create your models here.



class Ticket(models.Model):
    Client = models.ForeignKey('clients.Client',null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Used = models.NullBooleanField(null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Films = models.ManyToManyField('moteur.Film',null=True,blank=True)
    ImagesVente = models.ManyToManyField('moteur.ImageVente',null=True,blank=True)
    Packs = models.ManyToManyField('moteur.Pack',null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
