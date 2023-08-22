from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import User

from rest_framework.generics import (ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView)

from .serializers import UserSerializer, UserCreateSerializer, UserClientSerializer


# Class for apis by users

#
#
class UserListApiView(ListAPIView):
    """
    Obtiene todos los usuarios superusers y staff
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        # filter only superusers and staff
        return User.objects.filter(is_superuser=True).__or__(User.objects.filter(is_staff=True)).all()


class UserClientListApiView(ListAPIView):
    """
    Obtiene todos los usuarios clientes
    """
    serializer_class = UserClientSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        # filter only superusers and staff
        return User.objects.filter(is_superuser=False).__and__(User.objects.filter(is_staff=False)).all()


class UserCreateApiView(CreateAPIView):
    """
    Crea un usuario
    """
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.all()


class UserDeleteApiView(DestroyAPIView):
    """
    Elimina un usuario
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.all()

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if user == request.user:
            return Response({"detail": "You cannot delete your own account."}, status=status.HTTP_403_FORBIDDEN)

        # Verifica si el usuario autenticado es superusuario
        # y si el usuario a eliminar no es superusuario
        if not request.user.is_superuser and user.is_superuser:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


class UserUpdateApiView(UpdateAPIView):
    """
    Actualiza un usuario
    """
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return User.objects.all()


class UserSearchApiView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return User.objects.filter(name__icontains=kword).__or__(User.objects.filter(last_name__icontains=kword))


class UserRetrieveApiView(RetrieveAPIView):
    """
    Obtiene un usuario
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
