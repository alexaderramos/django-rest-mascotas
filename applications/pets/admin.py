from django.contrib import admin

from applications.pets.models import Pet, PetVaccine

# Register your models here.
admin.site.register(Pet)
admin.site.register(PetVaccine)
