from django.db import models
from django.forms import ModelForm, Textarea

class Cours(models.Model):
    '''
    Le cours doit obligatoirement être accompagné d'un document
    Un cours est publié par un utilisateur (motivé aha)
    Un cours peut être publié alors qu'il en existe déjà alors que cela traite du même sujet
    On invite l'utilisateur a condensé le plus possible ces cours

    TODO
    Penser à un système de rank
    '''
    titre = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    document = models.FileField(upload_to=None, max_length=100)



class CoursForm(ModelForm):
    class Meta:
        model = Cours
        fields =  "__all__"
        widgets = {
            "titre": Textarea(attrs={"cols": 80, "rows": 20}),
            "titre": Textarea(attrs={"cols": 80, "rows": 20}),
        }