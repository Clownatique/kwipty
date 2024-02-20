from django import forms
from compte.models import CardReview
from .models import FlashCarte

class FlashCarteForm(forms.ModelForm):

    class Meta:
        model = FlashCarte
        fields = ['tag','devant','image_devant','dos','image_dos']

class MajProchaineRevue(forms.ModelForm):
    class Meta:
        model = CardReview
        fields = ['difficulte']

    def __init__(self, *args, **kwargs):
        super(UpdateDue, self).__init__(*args, **kwargs)
        self.fields['difficulte'].widget = forms.RadioSelect(choices=DonnesRevision.facilite_reconnaissance)