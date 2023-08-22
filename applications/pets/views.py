from django.db.models import Q
from rest_framework import generics, permissions

from .models import Pet, PetVaccine
from .serializers import PetSerializer, PetDetailSerializer, PetVaccineSerializer, PetCreateSerializer, \
    PetVaccineCreateSerializer


class PetListApiView(generics.ListAPIView):
    """
    Obtiene todas las mascotas
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetCreateApiView(generics.CreateAPIView):
    """
    Crea una mascota
    """
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer


class PetRetrieveApiView(generics.RetrieveAPIView):
    """
    Obtiene una mascota
    """
    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer


class PetUpdateApiView(generics.UpdateAPIView):
    """
    Actualiza una mascota
    """
    queryset = Pet.objects.all()
    serializer_class = PetCreateSerializer


class PetDestroyApiView(generics.DestroyAPIView):
    """
    Elimina una mascota
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


# *************************************************** Pets Parents ***************************************************
class PetListByParentView(generics.ListAPIView):
    """
    Obtiene los hijos de una mascota
    """
    serializer_class = PetDetailSerializer

    def get_queryset(self):
        parent_id = self.kwargs['pet_id']
        return Pet.objects.filter(Q(father_id=parent_id) | Q(mother_id=parent_id))


class PetChildrenByParentView(generics.ListAPIView):
    """
    Obtiene los hijos de una mascota por padre y madre
    """
    serializer_class = PetSerializer

    def get_queryset(self):
        father_id = self.kwargs['father_id']
        mother_id = self.kwargs['mother_id']

        return Pet.objects.filter(Q(father_id=father_id) & Q(mother_id=mother_id))


class PetSiblingsListView(generics.ListAPIView):
    """
    Obtiene los hermanos de una mascota
    """
    serializer_class = PetSerializer

    def get_queryset(self):
        pet_id = self.kwargs['pet_id']
        try:
            pet = Pet.objects.get(pk=pet_id)
            if pet.father_id and pet.mother_id:
                return Pet.objects.filter(
                    Q(father_id=pet.father_id) | Q(mother_id=pet.mother_id)
                ).exclude(pk=pet_id)
            else:
                return Pet.objects.none()
        except Pet.DoesNotExist:
            return Pet.objects.none()


class PetListByOwnerView(generics.ListAPIView):
    """
    Obtiene las mascotas de un dueño
    """
    serializer_class = PetSerializer

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return Pet.objects.filter(owner_id=owner_id)


# *************************************************** Pets Vaccines ***************************************************

class PetVaccineListByPetView(generics.ListAPIView):
    """
    Obtiene las vacunas de una mascota
    """
    serializer_class = PetVaccineSerializer

    def get_queryset(self):
        pet_id = self.kwargs['pet_id']
        return PetVaccine.objects.filter(pet_id=pet_id)


#
# class PetVaccineListApiView(generics.ListAPIView):
#     """
#    (No usado)
#     """
#     queryset = PetVaccine.objects.all()
#     serializer_class = PetVaccineSerializer


class PetVaccineCreateApiView(generics.CreateAPIView):
    """
    Crea una vacuna para una mascota
    """
    queryset = PetVaccine.objects.all()
    serializer_class = PetVaccineCreateSerializer


# class PetVaccineRetrieveApiView(generics.RetrieveAPIView):
#     queryset = PetVaccine.objects.all()
#     serializer_class = PetVaccineSerializer
#
#
# class PetVaccineUpdateApiView(generics.UpdateAPIView):
#     queryset = PetVaccine.objects.all()
#     serializer_class = PetVaccineSerializer


class PetVaccineDestroyApiView(generics.DestroyAPIView):
    """
    Elimina una vacuna de una mascota
    """
    queryset = PetVaccine.objects.all()
    serializer_class = PetVaccineSerializer
