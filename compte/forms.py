from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Eleve
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.utils import timezone

class CreationElevesForms(UserCreationForm):
    class Meta:
        model = Eleve
        fields = UserCreationForm.Meta.fields + ('nom', 'prenom', 'email')

    def save(self, commit=True):
        utilisateur = super().save(commit=False)
        if commit:
            utilisateur.save()

        return utilisateur

class ChangeElevesForms(UserChangeForm):
    classes = [
        ('License - 1ere Année', 'L1'),
        ('Tale', 'Lycée - Terminale'),
        ('Lycée - Première', 'premiere')
    ]
    cursus_classe = forms.ChoiceField(choices=classes, required=True)
    
    class Meta:
        model = Eleve
        fields = UserCreationForm.Meta.fields + ('cursus_classe','nom', 'prenom', 'email')

    def save(self, commit=True):
        utilisateur = super().save(commit=False)

        cursus_classe = self.cleaned_data['cursus_classe']

        cursus = Cursus.objects.create(classes=cursus_classe)
        cursus.specialites.set(specialites)

        utilisateur.cursus = cursus

        if commit:
            utilisateur.save()

        return utilisateur

class LoginForm(AuthenticationForm):
    pass
