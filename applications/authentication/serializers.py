from abc import ABC

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from applications.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('name', 'password', 'email', 'last_name', 'document')

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            last_name=validated_data.get('last_name'),
            document=validated_data['document'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user:
            if not user.check_password(attrs['password']):
                raise serializers.ValidationError({'password': 'Contraseña incorrecta.'})
            return data
        else:
            raise serializers.ValidationError({'username': 'Usuario no encontrado.'})
