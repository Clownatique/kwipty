from django.urls import path
from . import views

urlpatterns = [
    path("cartes/nouvelle-carte.", views.creer_une_carte, name='creer-carte'),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes"),
    path("cartes/<str:flashcarteid>", views.reviser_carte, name="reviser-carte"),
    path("cartes/<str:flashcarteid>/update/", views.MajProchaineRevue, name="maj-metadonnes"),
]
