from rest_framework.generics import (
    ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView)
from rest_framework import permissions
from django.db import transaction

from utils.helpers import ResponseHelper
from .models import Specie
from .serializers import SpecieSerializer


class ListSpecieApiView(ListAPIView):
    serializer_class = SpecieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Specie.objects.all()


class SpecieRetrieveApiView(RetrieveAPIView):
    serializer_class = SpecieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Specie.objects.all()


class CreateSpecieApiView(CreateAPIView):
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Specie.objects.all()


class UpdateSpecieApiView(UpdateAPIView):
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Specie.objects.all()


class DeleteSpecieApiView(DestroyAPIView):
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Specie.objects.all()
