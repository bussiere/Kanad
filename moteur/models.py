from django.db import models
from django.db.models.signals import post_save
from pages.models import Page
from copy import deepcopy
# Create your models here.


class Currency(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Abreviation = models.CharField(max_length=5,null=True,blank=True)
    Symbole = models.CharField(max_length=5,null=True,blank=True)

class Prix(models.Model):
    Currency = models.ForeignKey('Currency')
    Abreviation = models.FloatField(null=True,blank=True)
   

class Avis(models.Model):
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Client = models.ForeignKey('clients.Client',null=True,blank=True)
    Publiable = models.NullBooleanField(blank=True)
    Note = models.FloatField(null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    def ___str__(self):
        return self.Client
    def __unicode__(self):
        return self.Client



class TypeImageItem(models.Model):
    Nom =  models.CharField(max_length=200,null=True,blank=True)


class ImageItem(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Type = models.ForeignKey('TypeImageItem',null=True,blank=True)

class TypeItem(models.Model):
    Nom =  models.CharField(max_length=200,null=True,blank=True)

class Item(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    #Code_Generee = models.CharField(max_length=1500,null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    Pub_date = models.DateTimeField('date published',null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Images = models.ManyToManyField('ImageFilm',null=True,blank=True)
    # Image principale representatve du film (a afficher lors des recherches, du panier, etc.,null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Mise_en_avant = models.CharField(max_length=200,null=True,blank=True)
    Acteurs = models.ManyToManyField('Acteur',null=True,blank=True)
    Lien = models.ManyToManyField('liens.Lien',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Avis = models.ManyToManyField(Avis,null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)
    TypeItem = models.ForeignKey('TypeItem',null=True,blank=True)

class ImageActeur(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)

    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    def save(self, *args, **kwargs):
        super(ImageActeur, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="ImageActeur_Modele"))
        page.pk = None
        page.Nom = self.Nom
        page.ImageActeur = self
        page.save()
	
class Acteur(models.Model):
    Pseudo = models.CharField(max_length=200,null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Image_Acteur = models.ManyToManyField(ImageActeur,null=True,blank=True)
    def ___str__(self):
    	return self.Pseudo
    def __unicode__(self):
        return self.Pseudo
    def save(self, *args, **kwargs):
        super(Acteur, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="Acteur_Modele"))
        #page.pk = None
        page.Nom = self.Pseudo
        page.Acteurs = [self]
        page.ImageActeur = self.Image_Acteur
        page.save()
 

class ApiLiee(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    IdApiObjet = models.CharField(max_length=200,null=True,blank=True)
    Api = models.ForeignKey('configuration.Api',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class TypeFilm(models.Model):
    Nom =  models.CharField(max_length=200,null=True,blank=True)

class TypeImageFilm(models.Model):
    Nom =  models.CharField(max_length=200,null=True,blank=True)

class ImageFilm(models.Model):
    ApiLiee = models.ManyToManyField(ApiLiee,null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    #Code_Generee = models.CharField(max_length=1500,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.ForeignKey('TypeImageFilm',null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Acteurs = models.ManyToManyField(Acteur,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)
    TypeFilm = models.ForeignKey('TypeFilm',null=True,blank=True)

    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    def save(self, *args, **kwargs):
        #super(Avis, self).save(*args, **kwargs) # Call the "real" save() method.
        super(ImageFilm, self).save(*args, **kwargs) 
        page = deepcopy(Page.objects.get(Nom="ImageFilm_Modele"))
        page.pk = None
        page.Nom = self.Nom
        page.Acteurs = self
        page.ImageActeur = self.Image_Acteur
        page.save()

class Film(models.Model):
    FilmApiLiee = models.ManyToManyField(ApiLiee,null=True,blank=True)
    FilmPreviewApiLiee = models.ManyToManyField(ApiLiee,related_name='Preview_Film',null=True,blank=True)
    URLFilmPreview = models.CharField(max_length=200,null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    #Code_Generee = models.CharField(max_length=1500,null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    Pub_date = models.DateTimeField('date published',null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Images = models.ManyToManyField(ImageFilm,null=True,blank=True)
    ImagesFilmPreview = models.ManyToManyField(ImageFilm,null=True,blank=True)
    # Image principale representatve du film (a afficher lors des recherches, du panier, etc.,null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Mise_en_avant = models.CharField(max_length=200,null=True,blank=True)
    Acteurs = models.ManyToManyField(Acteur,null=True,blank=True)
    Lien = models.ManyToManyField('liens.Lien',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Avis = models.ManyToManyField(Avis,null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)

    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    
    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="Film_Modele"))
        page.pk = None
        page.save()
        page.Nom = "%s_film"%self.Nom
        page.Film.add(self)
        page.ImageFilm = self.Images.all()
        page.save()
 


class ImageVente(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Film = models.ForeignKey(Film,null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Acteurs = models.ManyToManyField(Acteur,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Gratuit = models.NullBooleanField(blank=True)
    Avis = models.ManyToManyField(Avis,null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)

    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="ImageVente_Modele"))
        page.pk = None
        page.Nom = self.Nom
        page.Imageventes = self
        page.save()
 

   
class Pack(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Films = models.ManyToManyField(Film,null=True,blank=True)
    ImagesVente = models.ManyToManyField(ImageVente,null=True,blank=True)
    Date_Creation = models.DateTimeField('date creation',null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Presentation = models.ManyToManyField('presentation.ImageSite',null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Avis = models.ManyToManyField(Avis,null=True,blank=True)
    Prix = models.ForeignKey('Prix',null=True,blank=True)

    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    def save(self, *args, **kwargs):
        super(Pack, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="Pack_Modele"))
        page.pk = None
        page.Pack = self
        page.Nom = self.Nom
        page.ImagesVente = self.ImagesVente
        page.Films = self.Films
        page.save()


class ImageVideo(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Acteurs = models.ManyToManyField(Acteur,null=True,blank=True)
    Image = models.FileField(upload_to='media',null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ForeignKey('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom
    
    def save(self, *args, **kwargs):
        super(ImageVideo, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="ImageVideo_Modele"))
        page.pk = None
        page.ImageVideo = self
        page.Nom = self.Nom
        page.save()

class Video(models.Model):
    VideoApiLiee = models.ManyToManyField(ApiLiee,null=True,blank=True)
    VideoPreviewApiLiee = models.ManyToManyField(ApiLiee,related_name='Preview_video',null=True,blank=True)
    UrlVideoPreview = models.CharField(max_length=200,null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    Film = models.ManyToManyField(Film,null=True,blank=True)
    Tag = models.ManyToManyField('tags.Tag',null=True,blank=True)
    Pub_date = models.DateTimeField('date published',null=True,blank=True)
    Creation = models.DateTimeField('date published',null=True,blank=True)
    ImagesVideo = models.ManyToManyField(ImageVideo,null=True,blank=True)
    ImageFilm = models.ManyToManyField(ImageFilm,null=True,blank=True)
    # Image principale representatve de la video (a afficher lors des recherches, du panier, etc.,null=True,blank=True)
    FamilleTag = models.ManyToManyField('tags.FamilleTag',null=True,blank=True)
    Type = models.CharField(max_length=200,null=True,blank=True)
    Description_courte = models.CharField(max_length=200,null=True,blank=True)
    Description = models.CharField(max_length=400,null=True,blank=True)
    Valeur_Ticket = models.FloatField(null=True,blank=True)
    Mise_en_avant = models.CharField(max_length=200,null=True,blank=True)
    Acteurs = models.ManyToManyField(Acteur,null=True,blank=True)
    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',null=True,blank=True)
    Lien = models.ManyToManyField('liens.Lien',null=True,blank=True)
    Note_divers = models.ManyToManyField('notes.Note_divers',null=True,blank=True)
    Avis = models.ManyToManyField(Avis,null=True,blank=True)
    def ___str__(self):
    	return self.Nom
    def __unicode__(self):
        return self.Nom 
    
    def save(self, *args, **kwargs):
        super(Video, self).save(*args, **kwargs) # Call the "real" save() method.
        page = deepcopy(Page.objects.get(Nom="Pack_Modele"))
        page.pk = None
        page.Video = self
        page.Nom = self.Nom
        page.save()                                            






