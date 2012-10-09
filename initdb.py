
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()
from pages.models import Page, Template
import settings

t1 = Template(Nom="template_index",contenu="""bienvenue<br>
<a href="../logout/">logout</a>""")
t1.save()
p = Page(Nom="index")
p.save()
p.Template.add(t1)
p.save()

t2 = Template(Nom="template_indexvide",contenu="""   <form method="post" action=".">{% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="login" />
    </form>""")
t2.save()
p = Page(Nom="indexvide")
p.save()
p.Template.add(t2)
p.save()

t3 = Template(Nom="template_invitationvide",contenu="""   <form method="post" action=".">{% csrf_token %}
    <input type="text" name="codeinvitation">
    <input type="submit" value="Bienvenue" />
    </form>""")
t3.save()
p = Page(Nom="invitationvide")
p.save()
p.Template.add(t3)  
p.save()


t4 = Template(Nom="template_invitation",contenu="""   <form method="post" action=".">{% csrf_token %}
    <input type="text" name="Pseudo">
    <input type="text" name="Email">
    <input type="text" name="Password1">
    <input type="text" name="Password2">
    <input type="hidden" name="codeinvitation" value="{{ invitation.Code }}">
    <input type="submit" value="Bienvenue" />
    </form>""")
t4.save()
p = Page(Nom="invitation")
p.save()
p.Template.add(t4)
p.save()