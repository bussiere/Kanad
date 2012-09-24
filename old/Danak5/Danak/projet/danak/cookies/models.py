from django.db import models


class Date_Visite(models.Model):
    Date = models.DateTimeField('Date visite',null=True,blank=True)
    def ___str__(self):
    	return self.Date
    def __unicode__(self):
        return self.Date
class Cookie(models.Model):
    IP = models.ForeignKey('clients.IP',null=True,blank=True)
    Panier = models.ForeignKey('paniers.Panier',null=True,blank=True)
    Date_Creation = models.DateTimeField('date creation',null=True,blank=True)
    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)
    Historique_hack_css = models.ManyToManyField('clients.Site_hack_css',null=True,blank=True)
    def ___str__(self):
    	return self.IP
    def __unicode__(self):
        return self.IP
