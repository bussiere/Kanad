# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Avis'
        db.create_table('moteur_avis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Client'], null=True, blank=True)),
            ('Publiable', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['Avis'])

        # Adding M2M table for field Texte_contenu on 'Avis'
        db.create_table('moteur_avis_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_avis_Texte_contenu', ['avis_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'Avis'
        db.create_table('moteur_avis_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_avis_Note_divers', ['avis_id', 'note_divers_id'])

        # Adding model 'ImageActeur'
        db.create_table('moteur_imageacteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['ImageActeur'])

        # Adding M2M table for field Tag on 'ImageActeur'
        db.create_table('moteur_imageacteur_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imageacteur', models.ForeignKey(orm['moteur.imageacteur'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_imageacteur_Tag', ['imageacteur_id', 'tag_id'])

        # Adding M2M table for field FamilleTag on 'ImageActeur'
        db.create_table('moteur_imageacteur_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imageacteur', models.ForeignKey(orm['moteur.imageacteur'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_imageacteur_FamilleTag', ['imageacteur_id', 'familletag_id'])

        # Adding M2M table for field Texte_contenu on 'ImageActeur'
        db.create_table('moteur_imageacteur_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imageacteur', models.ForeignKey(orm['moteur.imageacteur'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_imageacteur_Texte_contenu', ['imageacteur_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'ImageActeur'
        db.create_table('moteur_imageacteur_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imageacteur', models.ForeignKey(orm['moteur.imageacteur'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_imageacteur_Note_divers', ['imageacteur_id', 'note_divers_id'])

        # Adding model 'Acteur'
        db.create_table('moteur_acteur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Pseudo', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['Acteur'])

        # Adding M2M table for field Tag on 'Acteur'
        db.create_table('moteur_acteur_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_acteur_Tag', ['acteur_id', 'tag_id'])

        # Adding M2M table for field FamilleTag on 'Acteur'
        db.create_table('moteur_acteur_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_acteur_FamilleTag', ['acteur_id', 'familletag_id'])

        # Adding M2M table for field Texte_contenu on 'Acteur'
        db.create_table('moteur_acteur_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_acteur_Texte_contenu', ['acteur_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'Acteur'
        db.create_table('moteur_acteur_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_acteur_Note_divers', ['acteur_id', 'note_divers_id'])

        # Adding M2M table for field Image_Acteur on 'Acteur'
        db.create_table('moteur_acteur_Image_Acteur', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False)),
            ('imageacteur', models.ForeignKey(orm['moteur.imageacteur'], null=False))
        ))
        db.create_unique('moteur_acteur_Image_Acteur', ['acteur_id', 'imageacteur_id'])

        # Adding model 'ImageFilm'
        db.create_table('moteur_imagefilm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['ImageFilm'])

        # Adding M2M table for field Tag on 'ImageFilm'
        db.create_table('moteur_imagefilm_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_imagefilm_Tag', ['imagefilm_id', 'tag_id'])

        # Adding M2M table for field FamilleTag on 'ImageFilm'
        db.create_table('moteur_imagefilm_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_imagefilm_FamilleTag', ['imagefilm_id', 'familletag_id'])

        # Adding M2M table for field Acteurs on 'ImageFilm'
        db.create_table('moteur_imagefilm_Acteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False))
        ))
        db.create_unique('moteur_imagefilm_Acteurs', ['imagefilm_id', 'acteur_id'])

        # Adding M2M table for field Texte_contenu on 'ImageFilm'
        db.create_table('moteur_imagefilm_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_imagefilm_Texte_contenu', ['imagefilm_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'ImageFilm'
        db.create_table('moteur_imagefilm_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_imagefilm_Note_divers', ['imagefilm_id', 'note_divers_id'])

        # Adding model 'Film'
        db.create_table('moteur_film', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Mise_en_avant', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['Film'])

        # Adding M2M table for field Tag on 'Film'
        db.create_table('moteur_film_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_film_Tag', ['film_id', 'tag_id'])

        # Adding M2M table for field Images on 'Film'
        db.create_table('moteur_film_Images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False))
        ))
        db.create_unique('moteur_film_Images', ['film_id', 'imagefilm_id'])

        # Adding M2M table for field FamilleTag on 'Film'
        db.create_table('moteur_film_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_film_FamilleTag', ['film_id', 'familletag_id'])

        # Adding M2M table for field Acteurs on 'Film'
        db.create_table('moteur_film_Acteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False))
        ))
        db.create_unique('moteur_film_Acteurs', ['film_id', 'acteur_id'])

        # Adding M2M table for field Lien on 'Film'
        db.create_table('moteur_film_Lien', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('lien', models.ForeignKey(orm['liens.lien'], null=False))
        ))
        db.create_unique('moteur_film_Lien', ['film_id', 'lien_id'])

        # Adding M2M table for field Texte_contenu on 'Film'
        db.create_table('moteur_film_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_film_Texte_contenu', ['film_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'Film'
        db.create_table('moteur_film_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_film_Note_divers', ['film_id', 'note_divers_id'])

        # Adding M2M table for field Avis on 'Film'
        db.create_table('moteur_film_Avis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False))
        ))
        db.create_unique('moteur_film_Avis', ['film_id', 'avis_id'])

        # Adding model 'ImageVente'
        db.create_table('moteur_imagevente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moteur.Film'], null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
            ('Gratuit', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['ImageVente'])

        # Adding M2M table for field Tag on 'ImageVente'
        db.create_table('moteur_imagevente_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_imagevente_Tag', ['imagevente_id', 'tag_id'])

        # Adding M2M table for field FamilleTag on 'ImageVente'
        db.create_table('moteur_imagevente_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_imagevente_FamilleTag', ['imagevente_id', 'familletag_id'])

        # Adding M2M table for field Acteurs on 'ImageVente'
        db.create_table('moteur_imagevente_Acteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False))
        ))
        db.create_unique('moteur_imagevente_Acteurs', ['imagevente_id', 'acteur_id'])

        # Adding M2M table for field Texte_contenu on 'ImageVente'
        db.create_table('moteur_imagevente_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_imagevente_Texte_contenu', ['imagevente_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'ImageVente'
        db.create_table('moteur_imagevente_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_imagevente_Note_divers', ['imagevente_id', 'note_divers_id'])

        # Adding M2M table for field Avis on 'ImageVente'
        db.create_table('moteur_imagevente_Avis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False))
        ))
        db.create_unique('moteur_imagevente_Avis', ['imagevente_id', 'avis_id'])

        # Adding model 'Pack'
        db.create_table('moteur_pack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Date_Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['Pack'])

        # Adding M2M table for field Films on 'Pack'
        db.create_table('moteur_pack_Films', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False))
        ))
        db.create_unique('moteur_pack_Films', ['pack_id', 'film_id'])

        # Adding M2M table for field ImagesVente on 'Pack'
        db.create_table('moteur_pack_ImagesVente', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('imagevente', models.ForeignKey(orm['moteur.imagevente'], null=False))
        ))
        db.create_unique('moteur_pack_ImagesVente', ['pack_id', 'imagevente_id'])

        # Adding M2M table for field FamilleTag on 'Pack'
        db.create_table('moteur_pack_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_pack_FamilleTag', ['pack_id', 'familletag_id'])

        # Adding M2M table for field Presentation on 'Pack'
        db.create_table('moteur_pack_Presentation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('imagesite', models.ForeignKey(orm['presentation.imagesite'], null=False))
        ))
        db.create_unique('moteur_pack_Presentation', ['pack_id', 'imagesite_id'])

        # Adding M2M table for field Tag on 'Pack'
        db.create_table('moteur_pack_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_pack_Tag', ['pack_id', 'tag_id'])

        # Adding M2M table for field Texte_contenu on 'Pack'
        db.create_table('moteur_pack_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_pack_Texte_contenu', ['pack_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'Pack'
        db.create_table('moteur_pack_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_pack_Note_divers', ['pack_id', 'note_divers_id'])

        # Adding M2M table for field Avis on 'Pack'
        db.create_table('moteur_pack_Avis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pack', models.ForeignKey(orm['moteur.pack'], null=False)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False))
        ))
        db.create_unique('moteur_pack_Avis', ['pack_id', 'avis_id'])

        # Adding model 'ImageVideo'
        db.create_table('moteur_imagevideo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('Lien', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liens.Lien'], null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['ImageVideo'])

        # Adding M2M table for field Tag on 'ImageVideo'
        db.create_table('moteur_imagevideo_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_imagevideo_Tag', ['imagevideo_id', 'tag_id'])

        # Adding M2M table for field FamilleTag on 'ImageVideo'
        db.create_table('moteur_imagevideo_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_imagevideo_FamilleTag', ['imagevideo_id', 'familletag_id'])

        # Adding M2M table for field Acteurs on 'ImageVideo'
        db.create_table('moteur_imagevideo_Acteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False))
        ))
        db.create_unique('moteur_imagevideo_Acteurs', ['imagevideo_id', 'acteur_id'])

        # Adding M2M table for field Texte_contenu on 'ImageVideo'
        db.create_table('moteur_imagevideo_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_imagevideo_Texte_contenu', ['imagevideo_id', 'texte_contenu_id'])

        # Adding M2M table for field Note_divers on 'ImageVideo'
        db.create_table('moteur_imagevideo_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_imagevideo_Note_divers', ['imagevideo_id', 'note_divers_id'])

        # Adding model 'Video'
        db.create_table('moteur_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Creation', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Type', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description_courte', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('Valeur_Ticket', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('Mise_en_avant', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('moteur', ['Video'])

        # Adding M2M table for field Film on 'Video'
        db.create_table('moteur_video_Film', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('film', models.ForeignKey(orm['moteur.film'], null=False))
        ))
        db.create_unique('moteur_video_Film', ['video_id', 'film_id'])

        # Adding M2M table for field Tag on 'Video'
        db.create_table('moteur_video_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('tag', models.ForeignKey(orm['tags.tag'], null=False))
        ))
        db.create_unique('moteur_video_Tag', ['video_id', 'tag_id'])

        # Adding M2M table for field ImagesVideo on 'Video'
        db.create_table('moteur_video_ImagesVideo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('imagevideo', models.ForeignKey(orm['moteur.imagevideo'], null=False))
        ))
        db.create_unique('moteur_video_ImagesVideo', ['video_id', 'imagevideo_id'])

        # Adding M2M table for field ImageFilm on 'Video'
        db.create_table('moteur_video_ImageFilm', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('imagefilm', models.ForeignKey(orm['moteur.imagefilm'], null=False))
        ))
        db.create_unique('moteur_video_ImageFilm', ['video_id', 'imagefilm_id'])

        # Adding M2M table for field FamilleTag on 'Video'
        db.create_table('moteur_video_FamilleTag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('familletag', models.ForeignKey(orm['tags.familletag'], null=False))
        ))
        db.create_unique('moteur_video_FamilleTag', ['video_id', 'familletag_id'])

        # Adding M2M table for field Acteurs on 'Video'
        db.create_table('moteur_video_Acteurs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('acteur', models.ForeignKey(orm['moteur.acteur'], null=False))
        ))
        db.create_unique('moteur_video_Acteurs', ['video_id', 'acteur_id'])

        # Adding M2M table for field Texte_contenu on 'Video'
        db.create_table('moteur_video_Texte_contenu', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('texte_contenu', models.ForeignKey(orm['presentation.texte_contenu'], null=False))
        ))
        db.create_unique('moteur_video_Texte_contenu', ['video_id', 'texte_contenu_id'])

        # Adding M2M table for field Lien on 'Video'
        db.create_table('moteur_video_Lien', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('lien', models.ForeignKey(orm['liens.lien'], null=False))
        ))
        db.create_unique('moteur_video_Lien', ['video_id', 'lien_id'])

        # Adding M2M table for field Note_divers on 'Video'
        db.create_table('moteur_video_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('note_divers', models.ForeignKey(orm['notes.note_divers'], null=False))
        ))
        db.create_unique('moteur_video_Note_divers', ['video_id', 'note_divers_id'])

        # Adding M2M table for field Avis on 'Video'
        db.create_table('moteur_video_Avis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('video', models.ForeignKey(orm['moteur.video'], null=False)),
            ('avis', models.ForeignKey(orm['moteur.avis'], null=False))
        ))
        db.create_unique('moteur_video_Avis', ['video_id', 'avis_id'])


    def backwards(self, orm):
        
        # Deleting model 'Avis'
        db.delete_table('moteur_avis')

        # Removing M2M table for field Texte_contenu on 'Avis'
        db.delete_table('moteur_avis_Texte_contenu')

        # Removing M2M table for field Note_divers on 'Avis'
        db.delete_table('moteur_avis_Note_divers')

        # Deleting model 'ImageActeur'
        db.delete_table('moteur_imageacteur')

        # Removing M2M table for field Tag on 'ImageActeur'
        db.delete_table('moteur_imageacteur_Tag')

        # Removing M2M table for field FamilleTag on 'ImageActeur'
        db.delete_table('moteur_imageacteur_FamilleTag')

        # Removing M2M table for field Texte_contenu on 'ImageActeur'
        db.delete_table('moteur_imageacteur_Texte_contenu')

        # Removing M2M table for field Note_divers on 'ImageActeur'
        db.delete_table('moteur_imageacteur_Note_divers')

        # Deleting model 'Acteur'
        db.delete_table('moteur_acteur')

        # Removing M2M table for field Tag on 'Acteur'
        db.delete_table('moteur_acteur_Tag')

        # Removing M2M table for field FamilleTag on 'Acteur'
        db.delete_table('moteur_acteur_FamilleTag')

        # Removing M2M table for field Texte_contenu on 'Acteur'
        db.delete_table('moteur_acteur_Texte_contenu')

        # Removing M2M table for field Note_divers on 'Acteur'
        db.delete_table('moteur_acteur_Note_divers')

        # Removing M2M table for field Image_Acteur on 'Acteur'
        db.delete_table('moteur_acteur_Image_Acteur')

        # Deleting model 'ImageFilm'
        db.delete_table('moteur_imagefilm')

        # Removing M2M table for field Tag on 'ImageFilm'
        db.delete_table('moteur_imagefilm_Tag')

        # Removing M2M table for field FamilleTag on 'ImageFilm'
        db.delete_table('moteur_imagefilm_FamilleTag')

        # Removing M2M table for field Acteurs on 'ImageFilm'
        db.delete_table('moteur_imagefilm_Acteurs')

        # Removing M2M table for field Texte_contenu on 'ImageFilm'
        db.delete_table('moteur_imagefilm_Texte_contenu')

        # Removing M2M table for field Note_divers on 'ImageFilm'
        db.delete_table('moteur_imagefilm_Note_divers')

        # Deleting model 'Film'
        db.delete_table('moteur_film')

        # Removing M2M table for field Tag on 'Film'
        db.delete_table('moteur_film_Tag')

        # Removing M2M table for field Images on 'Film'
        db.delete_table('moteur_film_Images')

        # Removing M2M table for field FamilleTag on 'Film'
        db.delete_table('moteur_film_FamilleTag')

        # Removing M2M table for field Acteurs on 'Film'
        db.delete_table('moteur_film_Acteurs')

        # Removing M2M table for field Lien on 'Film'
        db.delete_table('moteur_film_Lien')

        # Removing M2M table for field Texte_contenu on 'Film'
        db.delete_table('moteur_film_Texte_contenu')

        # Removing M2M table for field Note_divers on 'Film'
        db.delete_table('moteur_film_Note_divers')

        # Removing M2M table for field Avis on 'Film'
        db.delete_table('moteur_film_Avis')

        # Deleting model 'ImageVente'
        db.delete_table('moteur_imagevente')

        # Removing M2M table for field Tag on 'ImageVente'
        db.delete_table('moteur_imagevente_Tag')

        # Removing M2M table for field FamilleTag on 'ImageVente'
        db.delete_table('moteur_imagevente_FamilleTag')

        # Removing M2M table for field Acteurs on 'ImageVente'
        db.delete_table('moteur_imagevente_Acteurs')

        # Removing M2M table for field Texte_contenu on 'ImageVente'
        db.delete_table('moteur_imagevente_Texte_contenu')

        # Removing M2M table for field Note_divers on 'ImageVente'
        db.delete_table('moteur_imagevente_Note_divers')

        # Removing M2M table for field Avis on 'ImageVente'
        db.delete_table('moteur_imagevente_Avis')

        # Deleting model 'Pack'
        db.delete_table('moteur_pack')

        # Removing M2M table for field Films on 'Pack'
        db.delete_table('moteur_pack_Films')

        # Removing M2M table for field ImagesVente on 'Pack'
        db.delete_table('moteur_pack_ImagesVente')

        # Removing M2M table for field FamilleTag on 'Pack'
        db.delete_table('moteur_pack_FamilleTag')

        # Removing M2M table for field Presentation on 'Pack'
        db.delete_table('moteur_pack_Presentation')

        # Removing M2M table for field Tag on 'Pack'
        db.delete_table('moteur_pack_Tag')

        # Removing M2M table for field Texte_contenu on 'Pack'
        db.delete_table('moteur_pack_Texte_contenu')

        # Removing M2M table for field Note_divers on 'Pack'
        db.delete_table('moteur_pack_Note_divers')

        # Removing M2M table for field Avis on 'Pack'
        db.delete_table('moteur_pack_Avis')

        # Deleting model 'ImageVideo'
        db.delete_table('moteur_imagevideo')

        # Removing M2M table for field Tag on 'ImageVideo'
        db.delete_table('moteur_imagevideo_Tag')

        # Removing M2M table for field FamilleTag on 'ImageVideo'
        db.delete_table('moteur_imagevideo_FamilleTag')

        # Removing M2M table for field Acteurs on 'ImageVideo'
        db.delete_table('moteur_imagevideo_Acteurs')

        # Removing M2M table for field Texte_contenu on 'ImageVideo'
        db.delete_table('moteur_imagevideo_Texte_contenu')

        # Removing M2M table for field Note_divers on 'ImageVideo'
        db.delete_table('moteur_imagevideo_Note_divers')

        # Deleting model 'Video'
        db.delete_table('moteur_video')

        # Removing M2M table for field Film on 'Video'
        db.delete_table('moteur_video_Film')

        # Removing M2M table for field Tag on 'Video'
        db.delete_table('moteur_video_Tag')

        # Removing M2M table for field ImagesVideo on 'Video'
        db.delete_table('moteur_video_ImagesVideo')

        # Removing M2M table for field ImageFilm on 'Video'
        db.delete_table('moteur_video_ImageFilm')

        # Removing M2M table for field FamilleTag on 'Video'
        db.delete_table('moteur_video_FamilleTag')

        # Removing M2M table for field Acteurs on 'Video'
        db.delete_table('moteur_video_Acteurs')

        # Removing M2M table for field Texte_contenu on 'Video'
        db.delete_table('moteur_video_Texte_contenu')

        # Removing M2M table for field Lien on 'Video'
        db.delete_table('moteur_video_Lien')

        # Removing M2M table for field Note_divers on 'Video'
        db.delete_table('moteur_video_Note_divers')

        # Removing M2M table for field Avis on 'Video'
        db.delete_table('moteur_video_Avis')


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
        }
    }

    complete_apps = ['moteur']
