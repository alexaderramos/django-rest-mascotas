from rest_framework import generics

from applications.vaccines.models import Vaccine
from applications.vaccines.serializers import VaccineSerializer


# Create your views here.
class VaccineListApiView(generics.ListAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineCreateApiView(generics.CreateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineRetrieveApiView(generics.RetrieveAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineUpdateApiView(generics.UpdateAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer


class VaccineDestroyApiView(generics.DestroyAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
