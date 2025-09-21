from django.db import models

class Personas (models.Model):
    cod_persona = models.BigIntegerField(primary_key=True)
    nom_persona = models.CharField(max_length=50)
    ape_persona = models.CharField(max_length=50)
    fec_nac = models.DateField()
    