from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import FlashCarte, CardReview
from django.core import serializers
import uuid

class Eleve(AbstractUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    deck = models.ManyToManyField("quiz.CardReview")
    def __str__(self):
        return self.username
