from django.db import models
from django.utils import timezone


# Create your models here.


class Sex(models.Model):
    name = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now),
    updated_at = models.DateTimeField(auto_now=True, auto_created=False)

    class Meta:
        verbose_name = "Sexo"
        verbose_name_plural = "Sexos"

    def __str__(self):
        return self.name
