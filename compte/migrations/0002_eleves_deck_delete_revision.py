# Generated by Django 4.2.7 on 2024-02-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('compte', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleves',
            name='deck',
            field=models.ManyToManyField(to='quiz.cardreview'),
        ),
        migrations.DeleteModel(
            name='Revision',
        ),
    ]
