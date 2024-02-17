from django.db import models

class Cours(models.Model):
    titre = models.CharField(max_length=50)
    #cours_parent = models.ForeignKey(Cours, on_delete=models.CASCADE)
