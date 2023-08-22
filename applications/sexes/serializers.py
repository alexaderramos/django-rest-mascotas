from rest_framework import serializers
from .models import Sex


class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('name'):
            raise serializers.ValidationError({'name': 'Name field is required'})
        if Sex.objects.filter(name=attrs.get('name')).exists():
            raise serializers.ValidationError({'name': 'This sex is already registered'})
        return attrs
