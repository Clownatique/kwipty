from django.shortcuts import render, redirect
from .forms import CoursForm

def affichage_matiere(request):
    pass

def affichage_cours(request):
    pass

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