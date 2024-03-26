from django.shortcuts import render, redirect, get_object_or_404
from .models import FlashCarte, MetaDonneesCarte
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import FlashCarteForm, MajProchaineRevue
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from .forms import MajProchaineRevue
from compte.models import Eleve, DeckUtilisateur
from datetime import date

def maj_donnes_revision(request, revision_instance, cartereview_id):
    if request.method == "POST":
        form = MajProchaineRevue(request.POST)
        if form.is_valid():
            card_revue = DonnesRevision.objects.get(id=cartereview_id)
            difficulty = form.cleaned_data['difficulty']
            card_revue.update_review_date()
            return redirect('dashboard')

def voir_cartes(request):
    cartes = FlashCarte.objects.filter(publique=True)
    context = {
        'cartes':cartes
    }
    return render(request, 'quiz/liste toutes les cartes .html', context)

def voir_cartes_utilisateur(request):
    eleve = Eleve.objects.get(pk=request.user.id)
    deck = get_object_or_404(DeckUtilisateur, pk=request.user.id)
    cartes = MetaDonneesCarte.objects.filter(eleve=eleve)
    context = {
        'deck':deck.cartes,
        'cartes':cartes
    }
    return render(request, 'quiz/liste deck utilisateur.html', context)

def reviser_carte(request, flashcarteid):
    flashcarte = FlashCarte.objects.get(id = flashcarteid)
    context = {
        'carte':flashcarte
    }
    return render(request, 'quiz/carte.html', context)

def ajouter_carte(request, carteid):
    carte = FlashCarte.objects.get(id = carteid)
    eleve = Eleve.objects.get(id=request.user.id)
    temp_meta= MetaDonneesCarte.objects.create(carte=carte,
                                                eleve=eleve,
                                                date_de_revue=date.today(),
                                                phase=0)
    temp_meta.save()
    return redirect('voir-cartes')

def creer_une_carte(request):
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
    carteforme = FlashCarteForm(request.POST)
    if request.method == "POST":
        if carteforme.is_valid():
            carteforme.save()
            return redirect('voir-cartes')
    return render(request, 'quiz/creation_flashcarte.html',{'forme': carteforme})  