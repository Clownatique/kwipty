from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core import serializers
import uuid

class FlashCarte(models.Model):
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
    
    
class CardReview(models.Model):
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

    def update_review_date(self):
        # Mettez à jour la date de révision en fonction de la difficulté
        days_to_add = 0
        if self.apprise == False:
            if self.difficulty == 1:#FACILE
                self.review_date += timedelta(days=1)
                self.apprise = True
                self.save()
            elif self.difficulty == 2:#MOYEN
                if self.demiapprise:
                    self.review_date += timedelta(hours=12)
                    self.apprise = True
                    self.save()
                else:
                    self.review_date += timedelta(hours=3)
                    self.demiapprise = True
                    self.save()
            elif self.difficulty == 3:#DIFFICILE
                self.review_date += timedelta(minutes=2)
                self.save()
            elif self.difficulty == 4:#A REFAIRE
                self.review_date += timedelta(seconds=150)
                self.save()
        else:
            if self.difficulty == 1:#FACILE
                self.review_date *= timedelta(self.review_date*2.5)
                self.save()
            elif self.difficulty == 2:#MOYEN
                self.review_date *= timedelta(self.review_date*2.5)
                self.save()
            elif self.difficulty == 3:#DIFFICILE
                self.apprise = False
                self.review_date = timedelta()
                self.ease -= 0.1
                self.save()
            elif self.difficulty == 4:#A REFAIRE
                self.apprise= False
                self.review_date += timedelta(minutes=1)
                self.save()

    def save(self, *args, **kwargs):
        if self.date_de_revue >= timezone.now() - timedelta(days=3 * 30):
            self.apprise = True
        else:
            self.apprise = False

        super(CardReview, self).save(*args, **kwargs)
