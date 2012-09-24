from django.db import models
from django.contrib.auth.models import User
from presentation.models import Langue
from tags.models import Tag
from moteur.models import Video,Film,Pack,ImageVente
from notes.models  import Note_divers

class IP(models.Model):
	ipv = models.CharField(max_length=50,null=True,blank=True)
        def ___str__(self):
             return self.ipv
        def __unicode__(self):
             return self.ipv
    

class Date_Visite(models.Model):
    	Date = models.DateTimeField('Date visite',null=True,blank=True)
        def __str__(self):
            return self.Date
        def __unicode__(self):
            return self.Date
    

class Site_hack_css(models.Model):
    Site = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.site
    def __unicode__(self):
        return self.Site
       
class Parcour(models.Model):
	Liens_cliques = models.ManyToManyField('liens.Lien',null=True,blank=True)

class Anonymous(models.Model):
    Referer = models.CharField(max_length=1500,null=True,blank=True)
    Langue = models.ForeignKey(Langue,null=True,blank=True)
    IP = models.ForeignKey(IP,null=True,blank=True)
    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',blank=True,null=True)
    Historique_hack_css = models.ManyToManyField(Site_hack_css,null=True,blank=True)
    Parcour = models.ManyToManyField(Parcour,null=True,blank=True)
    def __str__(self):
        return self.IP
    def __unicode__(self):
        return self.IP
    

class Categorie_Client (models.Model):
    Nom  = models.CharField(max_length=200,blank=True,null=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',blank=True,null=True)
    
    def __str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom


	
class Client(models.Model):
    User = models.ForeignKey(User, unique=True,null=True,blank=True) 
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Prenom = models.CharField(max_length=200,null=True,blank=True)
    Email =  models.EmailField(null=True,blank=True)
    Telephone = models.CharField(max_length=200,null=True,blank=True)
    Date_inscription = models.DateTimeField('date inscription',null=True,blank=True)
    Naissance = models.DateTimeField('Date de naissance',null=True,blank=True)
    Tag = models.ManyToManyField(Tag,null=True,blank=True)
    Video_Vendu =  models.ManyToManyField(Video,null=True,blank=True)
    Film_Vendu = models.ManyToManyField(Film,null=True,blank=True)
    Pack_Vendu = models.ManyToManyField(Pack,null=True,blank=True)
    Imageventes_Vendu = models.ManyToManyField(ImageVente,null=True,blank=True)
    IP = models.ManyToManyField(IP,null=True,blank=True)
    Note_divers = models.ManyToManyField(Note_divers,null=True,blank=True)
    Referer = models.CharField(max_length=1500,null=True,blank=True)
    Langue = models.ManyToManyField(Langue,null=True,blank=True)
    Date_Visite = models.ManyToManyField(Date_Visite,null=True,blank=True)
    Abo_Newsletter = models.NullBooleanField(blank=True)
    Was_Anonymous = models.ForeignKey(Anonymous,null=True,blank=True)
    Categorie = models.ManyToManyField(Categorie_Client,null=True,blank=True)
    Historique_hack_css = models.ManyToManyField(Site_hack_css,null=True,blank=True)
    Parcour = models.ManyToManyField(Parcour,null=True,blank=True)
    def __str__(self):
        return self.Email
    def __unicode__(self):
        return self.Email
  
	
