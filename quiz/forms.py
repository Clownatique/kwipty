from django import forms
from compte.models import CardReview
from .models import FlashCarte

class FlashCarteForm(forms.ModelForm):

    class Meta:
        model = FlashCarte
        fields = ['tag','devant','image_devant','dos','image_dos']

class UpdateDue(forms.ModelForm):
    class Meta:
        model = CardReview
        fields = ['difficulty']

    def __init__(self, *args, **kwargs):
        super(UpdateDue, self).__init__(*args, **kwargs)
        self.fields['difficulty'].widget = forms.RadioSelect(choices=CardReview.DIFFICULTY_CHOICES)