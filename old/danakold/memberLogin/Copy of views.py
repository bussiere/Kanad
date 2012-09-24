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
def Login(request):
    user = request.user
    print user
    if not user.is_authenticated() :
        html = [request,'login.html',{'logged':'false'}]
        if request.method == 'POST' :
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            user = authenticate(username=email,password=password)
            print 'Second',user
        
        if user is not None :
            if user.is_active :
                print "You provided a correct username and password!"
                html = [request,'login.html',{'logged':'true', 'pseudo': 'Robert'}]
            else :
                print "Your account has been disabled!"
        else :
            print "Your username and password were incorrect."
    else :
        html = [request,'login.html',{'logged':'true', 'pseudo': 'Robert'}]
    
    return html

