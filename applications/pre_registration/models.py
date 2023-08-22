from django.db import models
from django.utils import timezone


# Create your models here.

class PreRegistration(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    consultation = models.TextField()
    pet_name = models.CharField(max_length=255)
    pet_specie = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pre registro"
        verbose_name_plural = "Pre registros"

    def __str__(self):
        return str(self.name + ' ' + self.last_name + ' - ' + self.email)
