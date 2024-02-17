from django.db import models

class Cours(models.Model):
    titre = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)