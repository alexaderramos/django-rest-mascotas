from rest_framework import serializers

from applications.pre_registration.models import PreRegistration


class PreRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreRegistration
        fields = '__all__'

    def validate(self, data):
        """
        Check that all fields are not empty and email is valid
        """
        if not data.get('name'):
            raise serializers.ValidationError({'name': "Name field is required."})
        if not data.get('last_name'):
            raise serializers.ValidationError("Last name field is required.")
        if not data.get('email'):
            raise serializers.ValidationError("Email field is required.")
        if not data.get('phone'):
            raise serializers.ValidationError("Phone field is required.")
        if not data.get('consultation'):
            raise serializers.ValidationError("Consultation field is required.")
        if not data.get('pet_name'):
            raise serializers.ValidationError("Pet name field is required.")
        if not data.get('pet_specie'):
            raise serializers.ValidationError("Pet species field is required.")
        if PreRegistration.objects.filter(email=data.get('email')).exists():
            raise serializers.ValidationError({'email': 'This email is already registered.'})
        return data
