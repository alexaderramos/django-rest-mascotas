from rest_framework import serializers

from applications.vaccines.models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'
