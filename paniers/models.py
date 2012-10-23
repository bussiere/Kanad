from django.db import models

# Create your models here.

class ItemAchat(models.Model):
    Films = models.ManyToManyField('moteur.Film',null=True,blank=True)
    ImagesVente = models.ManyToManyField('moteur.ImageVente',null=True,blank=True)
    Packs = models.ManyToManyField('moteur.Pack',null=True,blank=True)
    Date_Creation = models.DateTimeField('date creation',null=True,blank=True)
    Tickets = models.ManyToManyField('tickets.Ticket',null=True,blank=True)
    Date_paiement = models.DateTimeField('date paiement',null=True,blank=True)
    Total = models.FloatField(null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Item = models.ManyToManyField('moteur.Item',null=True,blank=True)
    

class Panier(models.Model):
    ItemAchat = models.ManyToManyField(ItemAchat,null=True,blank=True)
    Client = models.ForeignKey('clients.Client',null=True,blank=True)
    
    
    def ___str__(self):
    	return self.Client
    def __unicode__(self):
        return self.Client.Email
