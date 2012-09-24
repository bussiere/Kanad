from django.db import models

# Create your models here.


class Ratio(models.Model):
    Ratio = models.FloatField()
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    def __str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

#a revoir et a augmenter
class Regle(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Client = models.ManyToManyField('clients.Client',null=True,blank=True)
    TagVendeurs = models.ManyToManyField('tags.Tag',related_name="Tags Vendeurs",null=True,blank=True)
    TagMoins = models.ManyToManyField('tags.Tag',related_name="Tags Moins Vendeurs",null=True,blank=True)
    TagPref = models.ManyToManyField('tags.Tag',related_name="Tags Les Preferes",null=True,blank=True)
    FamilleTagVendeurs = models.ManyToManyField('tags.FamilleTag',related_name="Famille vendeurs",null=True,blank=True)
    FamilleTagMoins = models.ManyToManyField('tags.FamilleTag',related_name="Famille moins vendeur",null=True,blank=True)
    FamilleTagPref = models.ManyToManyField('tags.FamilleTag',related_name="famille Pref",null=True,blank=True)
    FilmPref = models.ManyToManyField('moteur.Film',related_name="film Pref",null=True,blank=True)
    FilmMoins = models.ManyToManyField('moteur.Film',related_name="film moins",null=True,blank=True)
    NouveauteFilm = models.ManyToManyField('moteur.Film',related_name="film nouveau",null=True,blank=True)
    PackPref = models.ManyToManyField('moteur.Pack',related_name="Pack Pref",null=True,blank=True)
    PackMoins = models.ManyToManyField('moteur.Pack',related_name="Pack moins",null=True,blank=True)
    NouveautePack = models.ManyToManyField('moteur.Pack',related_name="Pack nouveau",null=True,blank=True)
    ImageVentePref = models.ManyToManyField('moteur.ImageVente',related_name="ImageVente Pref",null=True,blank=True)
    ImageVenteMoins = models.ManyToManyField('moteur.ImageVente',related_name="ImageVente moins",null=True,blank=True)
    NouveauteImageVente= models.ManyToManyField('moteur.ImageVente',related_name="ImageVente nouveau",null=True,blank=True)
    Ratio = models.ManyToManyField('regles.Ratio',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    def __str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom


