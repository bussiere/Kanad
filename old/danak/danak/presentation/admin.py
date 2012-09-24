from presentation.models import Langue
from presentation.models import Categorie_Texte
from presentation.models import Texte
from presentation.models import Couleur
from presentation.models import Categorie_code
from presentation.models import Code
from presentation.models import StyleCss
from presentation.models import MiseEnForme
from presentation.models import Categorie_Texte_contenu
from presentation.models import Texte_contenu
from presentation.models import ImageSite
from presentation.models import Menu
from django.contrib import admin

admin.site.register(Langue)
admin.site.register(Categorie_Texte)
admin.site.register(Texte)
admin.site.register(Couleur)
admin.site.register(Categorie_code)
admin.site.register(Code)
admin.site.register(StyleCss)
admin.site.register(MiseEnForme)
admin.site.register(Categorie_Texte_contenu)
admin.site.register(Texte_contenu)
admin.site.register(ImageSite)
admin.site.register(Menu)

