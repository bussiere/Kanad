from django.db import models

# Create your models here.

class Categorie_Note(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom

class Note_divers(models.Model):
    Nom = models.CharField(max_length=400,null=True,blank=True)	
    texte_note = models.CharField(max_length=400,null=True,blank=True)
    Categorie = models.ForeignKey(Categorie_Note,null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom

