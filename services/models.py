from django.db import models

class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=255)
    specialites = models.CharField(max_length=255)
    description = models.TextField()
    adresse = models.CharField(max_length=255)
    est_actif = models.BooleanField(default=True)
    email = models.EmailField()
    date_de_creation = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(max_length=20)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nomcomplet
