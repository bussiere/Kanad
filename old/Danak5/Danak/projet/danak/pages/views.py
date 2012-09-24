# Create your views here.
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext 
from django.http import HttpResponse 
from pages.models import Page, Categorie_Page 
from moteur.models import Film 
from scripts_django.tools import recursif_template

def Index(request):
        page = Page.objects.get(Nom="index")
        films = Film.objects.all()
	t = ""
	for template in page.Template.all() :
		t += recursif_template(template.contenu)  
	t = Template(t)
        c = RequestContext(request, dict(page=page, films=films))
	html = t.render(c)#page.Template_Page.contenu
	return HttpResponse(html)

def Pages(request):
        page = Page.objects.get(Nom="index")
        film = Film.objects.all()
        
	t = ""
	for template in page.Template_Page.all() :
		t += recursif_template(template.contenu)  
	t = Template(t)
        c = RequestContext(request, dict(page=page, film=film))
	html = t.render(c)#page.Template_Page.contenu
	return HttpResponse(html)

def Films(request, pagefilm):
    page = Page.objects.get(Nom=pagefilm)
    t = ""
    filmnom = pagefilm.replace("_film", "")
    films = Film.objects.get(Nom=filmnom)
    for template in page.Template.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request, dict(page=page, films=films))
    html = t.render(c)#page.Template_Page.contenu
    return HttpResponse(html)

def Actors(request):
    page = Page.objects.get(Nom="index")
    t = ""
    for template in page.Template_Page.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request, dict(page=page))
    html = t.render(c)#page.Template_Page.contenu
    return HttpResponse(html)

def Packs(request):
    page = Page.objects.get(Nom="index")
    t = ""
    for template in page.Template_Page.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request, dict(page=page))

    html = t.render(c)#page.Template_Page.contenu
    return HttpResponse(html)
def ImageSe(request):
    page = Page.objects.get(Nom="index")
    t = ""
    for template in page.Template_Page.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request, dict(page=page))
    html = t.render(c)#page.Template_Page.contenu
    return HttpResponse(html)


