from django.urls import path
from . import views

urlpatterns = [
    path("nouveau-cours/", views.creer_cours, name="creer-cours"),
]
