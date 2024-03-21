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
    return render(request, 'quiz/blank.html', context)

def reviser_carte(request, cart):
    context = { 
        'form':form,
        'carte':carte_etudiee_dict,
        'revision':revision.id
    }
    return render(request, 'quiz/carte.html', context)

def creer_une_carte(request):
    return render(request, "../templates/quiz/creation_flashcarte.html")














#    revision= Revision.objects.get(id=revision_instance)
#    cartes_revues = revision.cartes.all()
#    liste = []
#    
#    flashcarte_instances = cartes_revues.values_list('carte', flat=True)
#    
#    # If you need the actual Flashcarte instances, you can use the 'in' filter
#    flashcarte_queryset = FlashCarte.objects.filter(pk__in=flashcarte_instances)
#
#    serialized_data = list(flashcarte_queryset.values())
#    json_data = json.dumps(serialized_data, cls=DjangoJSONEncoder)
#
#    context = {
#        'cartes':json_data,
#    }
#    
#    return render(request, 'quiz/carte.html', context)
#
