# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field Produits on 'Panier'
        db.create_table('paniers_panier_Produits', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('panier', models.ForeignKey(orm['paniers.panier'], null=False)),
            ('produit', models.ForeignKey(orm['moteur.produit'], null=False))
        ))
        db.create_unique('paniers_panier_Produits', ['panier_id', 'produit_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field Produits on 'Panier'
        db.delete_table('paniers_panier_Produits')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'clients.anonymous': {
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clients.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.IP']", 'null': 'True', 'blank': 'True'}),
            'Langue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presentation.Langue']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Anonymous'},
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clients.categorie_client': {
            'Meta': {'object_name': 'Categorie_Client'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clients.client': {
            'Abo_Newsletter': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clients.Categorie_Client']", 'null': 'True', 'blank': 'True'}),
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clients.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'Date_inscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'Film_Vendu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'Historique_hack_css': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clients.Site_hack_css']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['clients.IP']", 'null': 'True', 'blank': 'True'}),
            'Imageventes_Vendu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVente']", 'null': 'True', 'blank': 'True'}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Langue']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Client'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Pack_Vendu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Pack']", 'null': 'True', 'blank': 'True'}),
            'Prenom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'Video_Vendu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Video']", 'null': 'True', 'blank': 'True'}),
            'Was_Anonymous': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Anonymous']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clients.date_visite': {
            'Date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Date_Visite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clients.ip': {
            'Meta': {'object_name': 'IP'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipv': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'clients.site_hack_css': {
            'Meta': {'object_name': 'Site_hack_css'},
            'Site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'liens.categorielien': {
            'Meta': {'object_name': 'CategorieLien'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'liens.lien': {
            'Categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.CategorieLien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Lien'},
            'MiseEnForme': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.MiseEnForme']", 'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'moteur.acteur': {
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Image_Acteur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageActeur']", 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Acteur'},
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Pseudo': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.avis': {
            'Client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']", 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Avis'},
            'Note': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Publiable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.film': {
            'Acteurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Acteur']", 'null': 'True', 'blank': 'True'}),
            'Avis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Avis']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'ImagePrincipale': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image principale representative'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['moteur.ImageFilm']"}),
            'Images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageFilm']", 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Film'},
            'Mise_en_avant': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.imageacteur': {
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ImageActeur'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.imagefilm': {
            'Acteurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Acteur']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ImageFilm'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.imagevente': {
            'Acteurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Acteur']", 'null': 'True', 'blank': 'True'}),
            'Avis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Avis']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Film': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'Gratuit': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'Image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ImageVente'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.imagevideo': {
            'Acteurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Acteur']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ImageVideo'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.pack': {
            'Avis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Avis']", 'null': 'True', 'blank': 'True'}),
            'Date_Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Films': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'ImagesVente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVente']", 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Pack'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Presentation': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.ImageSite']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.produit': {
            'Film': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'ImageVente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVente']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Produit'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Pack': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Pack']", 'null': 'True', 'blank': 'True'}),
            'Video': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Video']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'moteur.video': {
            'Acteurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Acteur']", 'null': 'True', 'blank': 'True'}),
            'Avis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Avis']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Film': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'ImageFilm': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageFilm']", 'null': 'True', 'blank': 'True'}),
            'ImagesVideo': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVideo']", 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Video'},
            'Mise_en_avant': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Valeur_Ticket': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'notes.categorie_note': {
            'Meta': {'object_name': 'Categorie_Note'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'notes.note_divers': {
            'Categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notes.Categorie_Note']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Note_divers'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texte_note': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'})
        },
        'paniers.panier': {
            'Client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']", 'null': 'True', 'blank': 'True'}),
            'Date_Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Date_paiement': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Films': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'ImagesVente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVente']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Panier'},
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Packs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Pack']", 'null': 'True', 'blank': 'True'}),
            'Produits': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Produit']", 'null': 'True', 'blank': 'True'}),
            'Tickets': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tickets.Ticket']", 'null': 'True', 'blank': 'True'}),
            'Total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_code': {
            'Meta': {'object_name': 'Categorie_code'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_texte': {
            'Meta': {'object_name': 'Categorie_Texte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['notes.Note_divers']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_texte_contenu': {
            'Meta': {'object_name': 'Categorie_Texte_contenu'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.code': {
            'Categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presentation.Categorie_code']", 'null': 'True', 'blank': 'True'}),
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'Couleur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Couleur']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Code'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.couleur': {
            'CodeHexa': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Couleur'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.imagesite': {
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Description_courte': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.FamilleTag']", 'null': 'True', 'blank': 'True'}),
            'Image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'Lien': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['liens.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ImageSite'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tags.Tag']", 'null': 'True', 'blank': 'True'}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.langue': {
            'Abreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Langue'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.miseenforme': {
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MiseEnForme'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'StyleCss': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.StyleCss']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.stylecss': {
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Code']", 'null': 'True', 'blank': 'True'}),
            'Couleur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Couleur']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'StyleCss'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.texte': {
            'Categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presentation.Categorie_Texte']", 'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Langue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presentation.Langue']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Texte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.texte_contenu': {
            'Categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['presentation.Categorie_Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Texte_contenu'},
            'MiseEnForme': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.MiseEnForme']", 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Texte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'tags.familletag': {
            'Meta': {'object_name': 'FamilleTag'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tags.Tag']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tags.tag': {
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Tag'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tickets.ticket': {
            'Client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clients.Client']", 'null': 'True', 'blank': 'True'}),
            'Creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Films': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Film']", 'null': 'True', 'blank': 'True'}),
            'ImagesVente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.ImageVente']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Ticket'},
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['notes.Note_divers']", 'null': 'True', 'blank': 'True'}),
            'Packs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['moteur.Pack']", 'null': 'True', 'blank': 'True'}),
            'Used': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['paniers']
