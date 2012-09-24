import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.shortcuts import render,RequestContext
from django.http import HttpResponse
from pages.models import Page,Categorie_Page,Template
from moteur.models import Film
from scripts_django.tools import recursif_template
import settings


b = Page(Nom="ImageActeur_Modele")
b.save()
b = Page(Nom="Acteur_Modele")
b.save()
b = Page(Nom="ImageFilm_Modele")
b.save()
b = Page(Nom="Film_Modele")
b.save()
b = Page(Nom="ImageVente_Modele")
b.save()
b = Page(Nom="Pack_Modele")
b.save()
b = Page(Nom="ImageVideo_Modele")
b.save()
b = Page(Nom="Pack_Modele")
b.save()
b = Template(Nom="index",contenu="""<html>
<body>
<img src="/media/haruhi.jpg" /><br>
<img src="{{ STATIC_URL }}haruhi.jpg" /><br>
{% include titi %}
</body>
</html>""")
b.save()
b = Template(Nom="titi",contenu="""titi
{% include toto %}""")
b.save()
b = Template(Nom="toto",contenu="""toto""")
b.save()
b = Page(Nom="index",Template=Template.objects.get("index"))
b.save()
