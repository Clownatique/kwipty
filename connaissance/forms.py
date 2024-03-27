from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):

    parent = forms.ModelChoiceField(queryset = Cours.objects.filter(racine=True), label = "Matière")

    class Meta:
        model = Cours
        fields = "__all__"
        labels = {
            "titre": ("Titre de votre cours"),
        }
        help_texts = {
            "titre": ("Choisissez un titre SIMPLE et conscis."),
        }
        error_messages = {
            "titre": {
                "max_length": ("Choisissez un titre de moins de 20 lettres."),
            },
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