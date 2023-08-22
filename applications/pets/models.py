from django.db import models

from applications.sexes.models import Sex
from applications.species.models import Specie
from applications.users.models import User
from applications.vaccines.models import Vaccine


class Pet(models.Model):
    name = models.CharField(max_length=100)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    brith_date = models.DateField()
    photo = models.URLField(blank=True, null=True)
    father = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='father_pets',
                               verbose_name='padre')
    mother = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='mother_pets',
                               verbose_name='madre')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)


class PetVaccine(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_administered = models.DateField()

    class Meta:
        verbose_name = 'Vacuna de mascota'
        verbose_name_plural = 'Vacunas de mascotas'

    def __str__(self):
        return f"{self.pet.name} - {self.vaccine.name}"
