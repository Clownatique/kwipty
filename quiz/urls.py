from django.urls import path
from . import views

urlpatterns = [
    path("cartes/nouvelle-carte.", views.creer_une_carte, name='creer-carte'),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes"),
    path("cartes/<str:cartereview_id>", views.reviser_carte, name="reviser-carte"),
    path("cartes/<str:cartereview_id>/update/", views.MajProchaineRevue, name="maj-metadonnes"),
]
