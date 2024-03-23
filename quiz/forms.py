from django import forms
from compte.models import MetaDonneesCarte
from .models import FlashCarte

#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

class FlashCarteForm(forms.ModelForm):
    '''
    permets tout bonnement la création d'une flashcarte
    '''
    class Meta:
        model = FlashCarte
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FlashCarteForm, self).__init__(*args, **kwargs)
        self.fields['dos'].widget = '?'
        self.fields['devant'].widget = '?' 
        #le reste des champs, voir dans quiz/models.py
    def save(self, commit = True):
        pass

class MajProchaineRevue(forms.Form):
    '''
    enregistre la nouvelle revue d'une carte pour l'utilisateur
    '''
    class Meta:
        model = MetaDonneesCarte
        fields = ['difficulte']

    def __init__(self, *args, **kwargs):
        super(MajProchaineRevue, self).__init__(*args, **kwargs)
        self.fields['difficulte'].widget = forms.RadioSelect(choices=MetaDonneesCarte.facilite_reconnaissance)
