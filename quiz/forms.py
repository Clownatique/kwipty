from django import forms
from compte.models import MetaDonneesCarte
from .models import FlashCarte

#https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/

class FlashCarteForm(forms.ModelForm):

    class Meta:
        model = FlashCarte
        fields = ['type_de_note','devant','image_devant','dos','image_dos']

    def __init__(self, *args, **kwargs):
        super(MajProchaineRevue, self).__init__(*args, **kwargs)
        self.fields['difficulte'].widget = forms.RadioSelect(choices=MetaDonneesCarte.facilite_reconnaissance)

class MajProchaineRevue(forms.Form):
    class Meta:
        model = MetaDonneesCarte
        fields = ['difficulte']

    def __init__(self, *args, **kwargs):
        super(MajProchaineRevue, self).__init__(*args, **kwargs)
        self.fields['difficulte'].widget = forms.RadioSelect(choices=MetaDonneesCarte.facilite_reconnaissance)