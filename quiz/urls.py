from django.urls import path
from . import views

urlpatterns = [
    path("cartes/revision/", views.reviser_cartes_ajourdhui, name='reviser-cartes'),
    path("cartes/creer-carte/", views.creer_une_carte, name='creer-carte'),
    path("cartes/deck/", views.voir_deck, name="voir-deck-perso"),
    path("cartes/<str:flashcarteid>", views.reviser_carte, name="reviser-carte"),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes-disponibles"),
    path("cartes/liste/ajout/<int:carteid>", views.ajouter_carte, name="ajout-carte"),
]
