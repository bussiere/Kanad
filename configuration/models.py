from django.db import models

class ClefUser(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    ClefUser = models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom



class ClefApi(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    ClefApi= models.CharField(max_length=200,null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom


class CoupleClef(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    ClefUser = models.ManyToManyField('ClefUser',null=True,blank=True)
    ClefApi= models.ManyToManyField('ClefApi',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

class Api(models.Model):
    Nom = models.CharField(max_length=200,null=True,blank=True)
    CoupleClef = models.ManyToManyField('CoupleClef',null=True,blank=True)
    def ___str__(self):
        return self.Nom
    def __unicode__(self):
        return self.Nom

