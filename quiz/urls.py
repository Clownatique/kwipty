from django.urls import path
from . import views

urlpatterns = [
    path("cartes/nouvelle-carte/", views.creer_une_carte, name='creer-carte'),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes"),
    path("cartes/liste/perso/", views.voir_cartes_utilisateur, name="voir-cartes-perso"),
    path("cartes/liste/perso/ajout/<int:carteid>", views.ajouter_carte, name="ajout-carte"),
    path("cartes/<str:flashcarteid>", views.reviser_carte, name="reviser-carte"),
    path("cartes/<str:flashcarteid>/update/", views.MajProchaineRevue, name="maj-metadonnes"),
]
