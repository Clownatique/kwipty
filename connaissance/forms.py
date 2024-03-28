from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):

    parent = forms.ModelChoiceField(queryset = Cours.objects.filter(racine=True), label = "Matière")

    class Meta:
        model = Cours
        fields = "__all__"
        labels = {
            "titre": ("Titre de votre cours"),
            "parent": ("Titre de votre cours à la base "),
            "document": ("Titre de votre document"),
            "racine": ("cochez si c'est une matière")
        }
        help_texts = {
            "titre": ("Choisissez un titre SIMPLE et conscis."),
            "parent": ("un parent doit etre la base d'un cours "),
            "document": ("Choisissez un titre SIMPLE et conscis."),
            "racine": ("une matière est la base des parents ou des cours si il n'y a pas de parents")
        }
        error_messages = {
            "titre": {
                "max_length": ("Choisissez un titre de moins de 20 caractère."),
            },
            "document":{
                "max_lenght": ("Choisissez un titre de moins de 100 caractères."),
            }
        }

    disable_client_side_validation = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['titre'].required = False
        self.fields['parent'].required = False
        self.fields['document'].required = False

class CoursEditForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'document']