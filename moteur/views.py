from django_quicky import routing
from django_quicky import view


url, urlpatterns = routing()
 
 
urlpatterns.add_admin('admin/')



@url('^$')
@view(render_to='index.html')
def une_vue(request):
	return "toto"
 
 
# @url('/on/peut/cummuler/les/routes')
# @url('/une/regex/que/django/comprends')
# def une_vue(request):# Create your views here.
