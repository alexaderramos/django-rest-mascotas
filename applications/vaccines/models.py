from django.db import models


# Create your models here.
class Vaccine(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre de la vacuna
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'

    def __str__(self):
        return self.name
