from django.urls import path
from . import views

urlpatterns = [
    path("cartes/nouvelle-carte.", views.creer_une_carte, name='creer-carte'),
    path("cartes/liste/", views.voir_cartes, name="voir-cartes"),
    path("cartes/<uuid:revision_instance>/<str:cartereview_id>", views.reviser_carte, name="reviser_carte"),
    path("cartes/<uuid:revision_instance>/<str:cartereview_id>/update/", views.MajProchaineRevue, name="update_carte_review"),
]
