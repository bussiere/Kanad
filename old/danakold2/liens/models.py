from django.db import models

# Create your models here.

class CategorieLien(models.Model):
        Nom = models.CharField(max_length=200,null=True,blank=True)
        Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
	def ___str__(self):
             return self.Nom
        def __unicode__(self):
             return self.Nom

class Lien(models.Model):
        Categorie = models.ForeignKey(CategorieLien,null=True,blank=True)
	Nom = models.CharField(max_length=200,null=True,blank=True)
	url = models.CharField(max_length=500,null=True,blank=True)
	alt = models.CharField(max_length=400,null=True,blank=True)
	Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
	MiseEnForme = models.ManyToManyField('presentation.MiseEnForme',null=True,blank=True)
	Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
	def ___str__(self):
             return self.Nom
        def __unicode__(self):
             return self.Nom


