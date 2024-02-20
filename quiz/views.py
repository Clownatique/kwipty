from django.shortcuts import render, redirect
from .models import FlashCarte, CardReview
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import FlashCarteForm, UpdateDue
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse
from .forms import UpdateDue

def maj_donnes_revision(request, revision_instance, cartereview_id):
    if request.method == "POST":
        form = UpdateDue(request.POST)
        if form.is_valid():
            card_revue = CardReview.objects.get(id=cartereview_id)
            #revision = Revision.objects.get(id=revision_instance)

            difficulty = form.cleaned_data['difficulty']
            card_revue.update_review_date()
            #if card_revue.apprise == True: 
            #    revision.cartes.remove(card_revue)
            #    revision.save()

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

def reviser_certaines_cartes(request, revision_instance):#revision_instance c'est la liste des id des cartes reviews
    revision_instance = Revision.objects.get(pk=revision_instance)
    cartes_id = revision_instance.cartes.values_list('id', flat=True)
    liste_cartes_id = list(cartes_id)
    if revision_instance.cartes.count() == 0:
        return redirect('home')
    carte_index = cartes_id[0]
    return redirect('reviser_carte', revision_instance.id, carte_index)


















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
