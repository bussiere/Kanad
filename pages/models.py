from django.db import models

# Create your models here.


class Categorie_Page(models.Model):
    Nom  = models.CharField(max_length=200,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom

class Template(models.Model):
     Nom =  models.CharField(max_length=200,blank=True)
     contenu = models. TextField(max_length=80000,blank=True)
     Note_divers = models.ManyToManyField('notes.Note_divers',blank=True)
     def ___str__(self):
    	return self.Nom
     def __unicode__(self):
        return self.Nom
	
class Page(models.Model):
    Nom =  models.CharField(max_length=200,blank=True)
    Template = models.ManyToManyField(Template,null=True,blank=True)
    self_url = models.ForeignKey('liens.Lien',null=True,blank=True)
    Categorie = models.ForeignKey(Categorie_Page,null=True,blank=True)
    Liens = models.ManyToManyField('liens.Lien',related_name="Liens sur la page",null=True,blank=True)
    Nom = models.CharField(max_length=200)
    ImagesSite = models.ManyToManyField('presentation.ImageSite',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)	
    MiseEnForme = models.ManyToManyField('presentation.MiseEnForme',null=True,blank=True)
    Menu = models.ManyToManyField('presentation.Menu',null=True,blank=True)
    Avis = models.ManyToManyField('moteur.Avis',null=True,blank=True)
    Regle = models.ManyToManyField('regles.Regle',null=True,blank=True)
    Pack = models.ManyToManyField('moteur.Pack',null=True,blank=True)
    Imageventes = models.ManyToManyField('moteur.ImageVente',null=True,blank=True)
    Film = models.ManyToManyField('moteur.Film',null=True,blank=True)
    ImageFilm = models.ManyToManyField('moteur.ImageFilm',null=True,blank=True)
    ImageActeur = models.ManyToManyField('moteur.ImageActeur',null=True,blank=True)
    Acteurs = models.ManyToManyField('moteur.Acteur',null=True,blank=True)
    generated = models.DateTimeField('date published',blank=True,null=True)
    modified = models.DateTimeField('date modified',blank=True,null=True)
    protege = models.NullBooleanField(blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom	
