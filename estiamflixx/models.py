from django.db import models

# Create your models here.

class Serie(models.Model):
    titre = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=2000)
    realisateur = models.fields.CharField(max_length=30)
    annee_de_sortie = models.fields.IntegerField()
    nbre_episodes = models.fields.IntegerField()

class User(models.Model):
    nom  = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=2000)
    adresse_mail = models.fields.CharField(max_length=30)
    mdp = models.fields.CharField(max_length=100)