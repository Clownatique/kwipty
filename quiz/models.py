from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core import serializers

class FlashCarte(models.Model):
    '''
    Une flashcarte est le modèle avec toutes les données d'une carte en elle même
    Étant donné que cette carte peut être crée par un utilisateur
    -> Une flashcarte ne change pas en fonction de son utilisateur
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
    tag = models.CharField(max_length=20, choices=possible_tags)
    date_ajout = models.DateField(auto_now_add=True, null=True)
    devant = models.CharField(max_length=100, blank=True, null=True)
    image_devant = models.ImageField(upload_to='media/image_devant/', blank=True, null=True)
    dos = models.CharField(max_length=100, blank=True, null=True)
    image_dos = models.ImageField(upload_to='media/image_dos/', blank=True, null=True)
    id = models.AutoField(primary_key=True)

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
        return f'''{self.devant}[10:] - {self.dos}[10:]'''
    
    
class StudyNotes(models.Model):
    '''
    Une Info de revue de carte possède une foreign key à une carte et un utilisateur.
    Elle contient toutes les infos concernant une flashcarte et son utilisateur (date de revue, date d'ajout dans le deck...)
    '''
    DIFFICULTY_CHOICES = [
        (1, 'Facile'),
        (2, 'Moyen'),
        (3, 'Difficile'),
        (4, 'A Refaire immédiatement')
    ]
    carte = models.ForeignKey(FlashCarte, on_delete=models.CASCADE)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=2)
    date_de_revue = models.DateTimeField()
    apprise = models.BooleanField(default=False)
    demiapprise = models.BooleanField(default=False)
    ease = models.FloatField(default=2.5)

    def __str__(self):
        return f"CardReview {self.id}"

    def mise_à_jour_de_la_prochaine_revue(self):
        days_to_add = 0
        if self.apprise == False:
            if self.difficulty == 1:#FACILE
                self.date_de_revue += timedelta(days=1)
                self.apprise = True
                self.save()
            elif self.difficulty == 2:#MOYEN
                if self.demiapprise:
                    self.date_de_revue += timedelta(hours=12)
                    self.apprise = True
                    self.save()
                else:
                    self.date_de_revue += timedelta(hours=3)
                    self.demiapprise = True
                    self.save()
            elif self.difficulty == 3:#DIFFICILE
                self.date_de_revue += timedelta(minutes=2)
                self.save()
            elif self.difficulty == 4:#A REFAIRE
                self.date_de_revue += timedelta(seconds=150)
                self.save()
        else:
            if self.difficulty == 1:#FACILE
                self.date_de_revue *= timedelta(self.date_de_revue*2.5)
                self.save()
            elif self.difficulty == 2:#MOYEN
                self.date_de_revue *= timedelta(self.date_de_revue*2.5)
                self.save()
            elif self.difficulty == 3:#DIFFICILE
                self.apprise = False
                self.date_de_revue = timedelta()
                self.ease -= 0.1
                self.save()
            elif self.difficulty == 4:#A REFAIRE
                self.apprise= False
                self.date_de_revue += timedelta(minutes=1)
                self.save()

    def save(self, *args, **kwargs):
        if self.date_de_revue >= timezone.now() - timedelta(days=3 * 30):
            self.apprise = True
        else:
            self.apprise = False

        super(CardReview, self).save(*args, **kwargs)
