# Generated by Django 4.2.6 on 2024-03-26 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connaissance', '0004_alter_cours_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='cours',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='connaissance.cours'),
        ),
    ]