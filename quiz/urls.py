from django.urls import path
from . import views

urlpatterns = [
    path("cartes/liste/", views.voir_cartes, name="voir-cartes"),
    path("cartes/<uuid:revision_instance>/<str:cartereview_id>", views.reviser_carte, name="reviser_carte"),
    #path("cartes/<uuid:revision_instance>/<str:cartereview_id>/update/", views.updateDue, name="update_carte_review"),
]
