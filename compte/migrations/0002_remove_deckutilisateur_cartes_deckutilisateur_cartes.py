# Generated by Django 4.2.6 on 2024-03-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_flashcarte_image_devant_and_more'),
        ('compte', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deckutilisateur',
            name='cartes',
        ),
        migrations.AddField(
            model_name='deckutilisateur',
            name='cartes',
            field=models.ManyToManyField(to='quiz.flashcarte'),
        ),
    ]
