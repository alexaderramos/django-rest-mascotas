from datetime import datetime

from rest_framework import serializers

from .models import Pet, PetVaccine
from ..users.serializers import UserPetSerializer
from ..vaccines.serializers import VaccineSerializer
from django.utils import timezone


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def validate(self, data):

        # validar que padre y madre no sean iguales
        if data.get('father') and data.get('mother'):
            #
            father = data.get('father')
            mother = data.get('mother')
            specie = data.get('specie')

            #
            if father == mother:
                raise serializers.ValidationError({
                    'mother': "Father and mother cannot be the same.",
                    'father': "Father and mother cannot be the same.",
                })

            # validar que sean del mismo especie
            if father.specie != mother.specie:
                raise serializers.ValidationError({
                    "father": "Father and mother must be the same specie.",
                    "mother": "Father and mother must be the same specie."
                })

            if father.specie != specie or mother.specie != specie:
                raise serializers.ValidationError({
                    "specie": "Father and mother must be the same specie.",
                })

            # validar que sean del mismo sexo
            if father.sex == mother.sex:
                raise serializers.ValidationError('Father and mother cannot be of the same sex.')

        # validar que la fecha de cumplimiento no sea mayor a la fecha actual
        if data.get('brith_date'):
            # parse date
            birthdate = data.get('brith_date')
            # get current date
            current_date = timezone.now().date()
            fecha_objeto = datetime.strptime(str(birthdate), "%Y-%m-%d").date()
            if fecha_objeto > current_date:
                raise serializers.ValidationError({'brith_date': 'Birthdate cannot be greater than current date.'})
        return data

    def update(self, instance, validated_data):
        # validar que el padre no sea el mismo
        if validated_data.get('father'):
            father = validated_data.get('father')
            if father == instance:
                raise serializers.ValidationError({'father': 'Father cannot be the same.'})

        if validated_data.get('mother'):
            father = validated_data.get('mother')
            if father == instance:
                raise serializers.ValidationError({'mother': 'Father cannot be the same.'})

        return super().update(instance, validated_data)


class PetDetailSerializer(serializers.ModelSerializer):
    father = PetSerializer(read_only=True)
    mother = PetSerializer(read_only=True)
    owner = UserPetSerializer(read_only=True)

    # vaccines = VaccineSerializer(many=True)

    class Meta:
        model = Pet
        fields = '__all__'


class PetVaccineCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetVaccine
        fields = '__all__'


class PetVaccineSerializer(serializers.ModelSerializer):
    vaccine = VaccineSerializer(read_only=True)

    class Meta:
        model = PetVaccine
        fields = '__all__'
