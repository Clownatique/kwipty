from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreationElevesForms, LoginForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.shortcuts import redirect

def home(request):
    context ={
        'utilisateur':request.user
    }
    return render(request, 'compte/homepage.html', context)

class CustomLoginView(LoginView):
    template_name = 'compte/connexion.html'  # specify your login template
    form_class = LoginForm

class SignUpView(generic.CreateView):
    form_class = CreationElevesForms
    success_url = reverse_lazy("login")
    template_name = "compte/inscription.html"

def travail(request):
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