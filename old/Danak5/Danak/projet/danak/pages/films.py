from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Page,Categorie_Page
from paniers.models import Panier 
from django.contrib import auth
from clients.models import Client
from paniers.models import Panier
from moteur.models import Film
from memberLogin.views import Login
from django.http import Http404  


def Index(request):

    client = Client.objects.get(User = request.user)
    panier = None
    if client.Panier is Null :
    	client.Panier = Panier(Client=client)
    	panier = client.Panier
		
    html = render(request, 'films.html',{'panier': Panier, 'user': user})
    return HttpResponse(html)


def TestPanier(request) :
    
    user = request.user
    
    if not user.is_authenticated():
	# Afficher un message indiquant a l'utilisateur qu'il n'est pas connecte
       html = Login(request)
    else : 
       pass
       
       try:
           client = Client.objects.get(User = user) 
       except Client.DoesNotExist:
           raise Http404
       try:
           panier = Panier.objects.get(Client = client)
       except Panier.DoesNotExist:
           raise Http404
		
    if 'filmId' in request.GET:
	filmId = request.GET['filmId']
        film = Film.objects.get(Id = filmId)
	panier.add(film)
	
    films = Film.objects.all()
	
    heure = "???"
    
    html = render(request,'experience.html',{'films': Film.objects.all(), 'heure': heure})

    return HttpResponse(html)
