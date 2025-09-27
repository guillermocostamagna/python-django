from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str:
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fec_nac = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'
    