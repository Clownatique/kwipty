from django import forms
from .models import FlashCarte, MetaDonneesCarte

#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

class FlashCarteForm(forms.ModelForm):
    '''
    permets tout bonnement la création d'une flashcarte
    '''
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
    class Meta:
        model = MetaDonneesCarte
        fields = ['difficulte']

    def __init__(self, *args, **kwargs):
        super(MajProchaineRevue, self).__init__(*args, **kwargs)
        self.fields['difficulte'].widget = forms.RadioSelect(choices=MetaDonneesCarte.facilite_reconnaissance)
