from django.db import models


# Create your models here.


class Stat(models.Model):
    Date = models.DateTimeField('date stat',null=True,blank=True)
    ip = models.ForeignKey('clients.IP',null=True,blank=True)
    client = models.ForeignKey('clients.Client',null=True,blank=True)
    anonymous = models.ForeignKey('clients.Anonymous',null=True,blank=True)
    Page = models.ManyToManyField('pages.Page',null=True,blank=True)
    Liens = models.ManyToManyField('liens.Lien',related_name="Liens Parcouru",null=True,blank=True)
    ImagesSite = models.ManyToManyField('presentation.ImageSite',null=True,blank=True)
    Menu = models.ManyToManyField('presentation.Menu',null=True,blank=True)
    Avis = models.ManyToManyField('moteur.Avis',null=True,blank=True)
    Regle = models.ManyToManyField('regles.Regle',null=True,blank=True)
    PackConsult = models.ManyToManyField('moteur.Pack',null=True,blank=True)
    ImageventesConsult = models.ManyToManyField('moteur.ImageVente',null=True,blank=True)
    FilmConsult = models.ManyToManyField('moteur.Film',null=True,blank=True)
    ImageFilm = models.ManyToManyField('moteur.ImageFilm',null=True,blank=True)
    ImageActeur = models.ManyToManyField('moteur.ImageActeur',null=True,blank=True)
    Acteur = models.ManyToManyField('moteur.Acteur',null=True,blank=True)
    VideoConsult =  models.ManyToManyField('moteur.Video',null=True,blank=True)
    ImageVideo = models.ManyToManyField('moteur.ImageVideo',null=True,blank=True)
    Video_Vendu =  models.ManyToManyField('moteur.Video',related_name="VideoVendu",null=True,blank=True)
    Film_Vendu = models.ManyToManyField('moteur.Film',related_name="FilmVendu",null=True,blank=True)
    Pack_Vendu = models.ManyToManyField('moteur.Pack',related_name="PackVendu",null=True,blank=True)
    Imageventes_Vendu = models.ManyToManyField('moteur.ImageVente',related_name="ImageVenteVendu",null=True,blank=True)
    Nom = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom





