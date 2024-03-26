# Generated by Django 4.2.6 on 2024-03-25 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlashCarte',
            fields=[
                ('type_de_note', models.CharField(choices=[('Date', 'Date'), ('Personnage/Figure', 'Personnage/Figure'), ('Formule', 'Formule'), ('Définition', 'Définition'), ('Mot', 'Mot'), ('Verbe', 'Verbe'), ('Citation', 'Citation'), ('Généralité', 'Généralité')], max_length=20)),
                ('date_ajout', models.DateField(auto_now_add=True, null=True)),
                ('devant', models.CharField(blank=True, max_length=100, null=True)),
                ('image_devant', models.ImageField(blank=True, null=True, upload_to='media/image_devant/')),
                ('dos', models.CharField(blank=True, max_length=100, null=True)),
                ('image_dos', models.ImageField(blank=True, null=True, upload_to='media/image_dos/')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('champs_supplementaires', models.TextField(blank=True, null=True)),
                ('publique', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaquetCartes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('cartes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.flashcarte')),
            ],
        ),
        migrations.CreateModel(
            name='MetaDonneesCarte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autoevaluation_possible', models.IntegerField(choices=[(1, 'Facile'), (2, 'Moyen'), (3, 'Difficile'), (4, 'A Refaire immédiatement')], default=2)),
                ('phase', models.IntegerField(choices=[(1, 'Facile'), (2, 'Moyen'), (3, 'Difficile'), (4, 'A Refaire immédiatement')], default=0)),
                ('facilitee_apprentissage', models.FloatField(default=2.5)),
                ('intervalle', models.CharField(default=0, max_length=4)),
                ('date_de_revue', models.DateTimeField()),
                ('carte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.flashcarte')),
            ],
        ),
    ]
