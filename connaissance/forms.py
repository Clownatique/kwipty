from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):

    parent = forms.ModelChoiceField(queryset = Cours.objects.filter(racine=True), label = "Matière")

    class Meta:
        model = Cours
        fields = "__all__"
        labels = {

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].required = False
        self.fields['document'].required = False