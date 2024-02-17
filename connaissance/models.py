from django.db import models

class Cours(models.Model):
    cours_parent = models.ForeignKey(on_delete=CASCADE)
