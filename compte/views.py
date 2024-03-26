from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreationEleveForms, LoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import redirect
from compte.models import DeckUtilisateur

def page_accueil(request):
    '''
    Une page d'accueil, pour les nouveaux utilisateur (ou non connecté)
    
    '''
    context ={
        'utilisateur':request.user
    }
    return render(request, 'compte/homepage.html', context)

class CustomLoginView(LoginView):
    template_name = 'compte/connexion.html'  # specify your login template
    form_class = LoginForm

class SignUpView(generic.CreateView):
    form_class = CreationEleveForms
    success_url = reverse_lazy("connexion")
    template_name = "compte/inscription.html"

def menu_principal(request):
    '''
    VIEW 'DASHBOARD' : 
    renvoie la page d'accueil de l'utilisateur connecté qui s'apprête à réviser

    Tout est prêt pour lui:
    quelques données pour lui rappeller ce qu'il va avoir réviser
    (nombre de cartes, temps de révision estimé selon son temps passé sur une carte)
    https://www.justinmind.com/ui-design/dashboard-design-best-practices-ux
    '''
    if request.user.is_authenticated:
        deck = DeckUtilisateur.objects.get(pk = request.user.id)
        context = {
            'deck':deck
        }

        return render(request, 'compte/dashboard.html', context)
    else:
        return render(request, 'pasconnecte.html')

def menu_tuto(request):
    '''
    Ici faire une page TRÈS IMPORTANTE pour l'ux:

    le tutoriel du menu principal.

    cette page va, à l'aide de plusieurs pages html,
    reprendre le menu principal afin d'en faire un tour complet.

    TODO:
    - Si l'utilisateur a déjà vu cette page, lui demander si il a besoin de le revoir ou si il a juste malcliqué
    '''


    pass