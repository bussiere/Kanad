# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.shortcuts import render,RequestContext
from django.http import HttpResponse
from pages.models import Page,Categorie_Page
from moteur.models import Film
from django.contrib.auth import authenticate
# from scripts.tools import recursif_template
def Login(request) :
    formulaire = """<form action="." method="POST"><strong>Courriel</strong> : <input type="text" name="email"> </br><strong>Mot de passe</strong> : <input type="password" name="password"> </br><input type="submit" value="Connexion"></form>"""
    if 'email' and 'password' in request.GET:
        email = request['email']
        password = request['password']
        user = authenticate(username=email,password=password)
        if user is not None :
            formulaire = None
        else :        
            if password != "" or email != "" :
                formulaire += "<br><br>Les informations que vous avez rentre sont erronnees"    
    
    return formulaire
