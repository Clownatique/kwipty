from django.shortcuts import render, redirect
from .forms import CoursForm
from .models import Cours

def liste_cours(request):
    matieres = Cours.objects.filter(racine=True)
    courses_by_subject = {}
    for matiere in matieres:
        courses_by_subject[matiere] = Cours.objects.filter(parent=matiere)
    return render(request, 'cours/liste.html', {'cours': courses_by_subject, 'matieres': matieres})

def affichage_cours(request, idcours):
    cours = Cours.objects.get(idcours)
    return render(request, 'cours/cours.html', {'cours':cours})

def creer_cours(request):
    if request.method =='POST':
        form = CoursForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            form = CoursForm(request.POST)
    context = {'forme':CoursForm(request.POST)}
    return render(request,  'cours/creer_cours.html', context)

def modifier_cours(request):
    if request.method =='POST':
        form = CoursEditForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            form = CoursForm(request.POST)
    context = {'forme':CoursForm(request.POST)}
    return render(request,  'cours/creer_cours.html', context)