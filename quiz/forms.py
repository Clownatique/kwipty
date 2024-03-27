from django import forms
from .models import FlashCarte, MetaDonneesCarte
from connaissance.models import Cours 

#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

class FlashCarteForm(forms.ModelForm):
    '''
    permets tout bonnement la création d'une flashcarte
    '''
    cours = forms.ModelChoiceField(queryset = Cours.objects.all(), label='Cours')
    class Meta:
        model = FlashCarte
        fields = '__all__'
#        labels = {
#            "dos": ("Writer"),
#        }
#        help_texts = {
#            "dos": ("Some useful help text."),
#        }
#        error_messages = {
#            "dos": {
#                "max_length": ("La question ne doit pas excèder tant de charactère."),
#            },
#        }

    def __init__(self, *args, **kwargs):
        super(FlashCarteForm, self).__init__(*args, **kwargs)

class MajProchaineRevue(forms.Form):
    '''
    enregistre la nouvelle revue d'une carte pour l'utilisateur
    '''
    autoevaluation_possible = forms.ChoiceField(choices=MetaDonneesCarte.facilite_reconnaissance, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(MajProchaineRevue, self).__init__(*args, **kwargs)

    def save(self):
        if self.instance:
            autoevaluation = self.cleaned_data.get('autoevaluation_possible')
            self.instance.maj_prochaine_revue(autoevaluation)
            self.instance.save()