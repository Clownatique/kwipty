from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import FlashCarte, PaquetCartes
from django.core import serializers
import uuid

class Eleve(AbstractUser):
    '''
    Un eleve = un utilisateur.
    TODO:
    Peut être rajouté des infos par rapport au niveau d'étude
    Réfléchir à un système de score
    '''
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    #deck = models.OneToOneField(DeckUtilisateur, on_delete=models.CASCADE, default=create_deck_instance())
    
    def __str__(self):
        return self.username

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        DeckUtilisateur.objects.create(eleve=self)

class DeckUtilisateur(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    cartes = models.ForeignKey(FlashCarte, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = ("Deck de l'utilisateur")
        verbose_name_plural = ("Decks des utilisateurs")

    def __str__(self):
        return f'''{self.eleve}'s deck'''

    def get_absolute_url(self):
        return reverse("DeckUtilisateur_detail", kwargs={"pk": self.pk})


def create_deck_instance():
    return DeckUtilisateur.objects.create()
