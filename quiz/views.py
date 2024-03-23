from django.shortcuts import render, redirect
from .models import FlashCarte, MetaDonneesCarte
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import FlashCarteForm, MajProchaineRevue
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from .forms import MajProchaineRevue

def maj_donnes_revision(request, revision_instance, cartereview_id):
    if request.method == "POST":
        form = MajProchaineRevue(request.POST)
        if form.is_valid():
            card_revue = DonnesRevision.objects.get(id=cartereview_id)
            difficulty = form.cleaned_data['difficulty']
            card_revue.update_review_date()
            return redirect('dashboard')

def voir_cartes(request):
    cartes = FlashCarte.objects.all()
    context = {
        'cartes':cartes
    }
    return render(request, 'quiz/nouveau carte momo.html', context)

def reviser_carte(request, flashcarteid):
    flashcarte = FlashCarte.objects.get(id = flashcarteid)
    context = {
        'carte':flashcarte
    }
    return render(request, 'quiz/carte.html', context)

class creer_une_carte(FlashCarteForm):
    '''
    Views qui va afficher le template de victor pour créer une carte
    Inspire toi au maximum de ce que tu vois dans l'application compte.
    Si il y a des problèmes, je t'ai envoyé des ressources pouvant aider.
    voir urls.py pour faire en sorte de rendre ce formulaire accessible,
    models.py pour comprendre ce que tu dois demander à l'utilisateur,
    et bien évidemment forms.py là ou tu dois faire tout cela.

    edit :
    je viens de peu à peu de comprendre qu'il y a plusieurs manières de faire 
    des forms. (en passant par model.py, views.py, ou forms.py).

    Concentre toi sur cette dernière
    '''
    template_name = 'quiz/creation_flashcarte.html'  # specify your login template
    form_class = FlashCarteForm