from rest_framework import serializers

from applications.species.models import Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = '__all__'

    def validate(self, data):
        if not data.get('name'):
            raise serializers.ValidationError({'name': 'Name field is required.'})
        if Specie.objects.filter(name=data.get('name')).exists():
            raise serializers.ValidationError({'name': 'This specie is already registered.'})
        return data
