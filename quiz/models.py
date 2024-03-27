from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.db import models
from django.utils import timezone
from datetime import timedelta

class FlashCarte(models.Model):
    '''
    Une flashcarte est le modèle avec toutes les données d'une carte en elle même
    Étant donné que cette carte peut être crée par un utilisateur
    -> Une flashcarte ne change pas en fonction de son utilisateur

    TODO : 
    RAJOUT CHAMP selon utilisateur(comme exemple utilisation..)
    
    '''
    possible_tags = [
        ('Date', 'Date'),
        ('Personnage/Figure', 'Personnage/Figure'),
        ('Formule', 'Formule'),
        ('Définition', 'Définition'),
        ('Mot', 'Mot'),
        ('Verbe', 'Verbe'),
        ('Citation', 'Citation'),
        ('Généralité','Généralité')
    ]
    type_de_note = models.CharField(max_length=20, choices=possible_tags)
    date_ajout = models.DateField(auto_now_add=True, null=True)
    devant = models.CharField(max_length=100, blank=True, null=True)
    image_devant = models.ImageField(upload_to='media/image_devant/', blank=True, null=True)
    dos = models.CharField(max_length=100, blank=True, null=True)
    image_dos = models.ImageField(upload_to='media/image_dos/', blank=True, null=True)
    id = models.AutoField(primary_key=True)
    champs_supplementaires = models.TextField(blank=True, null = True)
    publique = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.image_devant:
            self.save_image(self.image_devant, 'image_devant')

        if self.image_dos:
            self.save_image(self.image_dos, 'image_dos')

        super(FlashCarte, self).save(*args, **kwargs)

    def save_image(self, image, attribute_name):
        image_name = f'{attribute_name}_{self.id}_{image.name}'
        self.__dict__[attribute_name] = f'images/{image_name}'
        if isinstance(image, ContentFile):
            with open(self.image_devant.path, 'wb') as f:
                f.write(image.read())
        elif isinstance(image, ImageFile):
            image.save(self.image_devant.path, image)
    
    def __str__(self):
        return f'''{self.devant}'''[:10] + f'''{self.dos}'''[:10]

class PaquetCartes(models.Model):
    '''Un paquet (le plus souvent à réviser) est comme son nom l'indique un paquet de carte.
    Il est relatif à plusieurs Données de révision

    A ne pas confondre avec un paquet de carte!!

    /!\ SUREMENT BIENTOT A SUPPRIMER

    '''
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    cartes = models.ForeignKey(FlashCarte, on_delete=models.CASCADE, null=True)
    #stats
    
class MetaDonneesCarte(models.Model):
    '''
    Les donnés de révision est lié à une carte pour un utilisateur.
    Elle précise tout ce que le backend a besoin concernant l'apprentissage de cette carte 
    (date de revue)

    TODO:
    Lire https://en.wikipedia.org/wiki/Leitner_system
    (ça équivaut à tout entièrement refaire mdr)
    '''
    facilite_reconnaissance = [
        (1, 'Facile'),  # La carte a été facilement assimilée
        (2, 'Moyen'),   # '' moyennement assimilée
        (3, 'Difficile'),
        (4, 'A Refaire immédiatement') # L'utilisateur souhaite explicitement revoir cette carte
    ]
    phases = [
        (0, 'Apprentissage'), # ICI on apprend comme si c'était nouveau
        (1, 'Approfondissement')
    ]

    carte = models.ForeignKey(FlashCarte, on_delete=models.CASCADE)
    eleve = models.ForeignKey("compte.Eleve", on_delete=models.CASCADE, null=True)
    autoevaluation_possible = models.IntegerField(choices=facilite_reconnaissance, default=2)
    phase = models.IntegerField(choices=phases, default=0)  # Utilisation de la liste 'phases' pour les choix
    facilitee_apprentissage = models.FloatField(default=2.5)
    intervalle = models.CharField(max_length=4, default=0, null=False, blank=False)
    date_de_revue = models.DateTimeField()

    def __str__(self):
        return f"DonnesRevision {self.id}"

    def maj_prochaine_revue(self, autoevaluation):
        '''
        fonction qui peut changer la date de revue, l'intervalle, la facilitee, la phase 
        EN FONCTION de l'utilisateur
        '''
        pass
