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
    success_url = reverse_lazy("login")
    template_name = "compte/inscription.html"

def menu_principal(request):
    '''
    VIEW 'DASHBOARD' : 
    renvoie la page d'accueil de l'utilisateur connecté qui s'apprête à réviser

    Tout est prêt pour lui:
    quelques données pour lui rappeller ce qu'il va avoir réviser
    (nombre de cartes, temps de révision estimé selon son temps passé sur une carte)
    '''
    if request.user.is_authenticated:
        liste_matieres_par_categorie = []

        context = {
            #'matiere': matiere,
            #'liste_cours':liste_cours,
            #'cartes':cartes_utilisateur_cours,
            #'cartes_non_apprises':cartes_utilisateur_cours,
            #'nombre_cartes_apprises':nombre_cartes_apprises,
            #'tag_counts':tag_counts,
            #'exercices':exercices,
            "liste_matieres_par_categorie": liste_matieres_par_categorie
        }
        template = loader.get_template('compte/dashboard.html')

        return HttpResponse(template.render(context,request))
    else:
        return render(request, 'pasconnecte.html')