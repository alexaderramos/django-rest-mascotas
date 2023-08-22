from django.db import transaction
from rest_framework import generics, permissions, status

from applications.pre_registration.models import PreRegistration
from applications.pre_registration.serializers import PreRegistrationSerializer
from utils.helpers import EmailHelper, ResponseHelper


# Create your views here.

# view to list and create pre-registration
class ListPreRegistrationAPIView(generics.ListAPIView):
    serializer_class = PreRegistrationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        data = PreRegistration.objects.all()
        return data

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return ResponseHelper.success_response(
            data=serializer.data,
            message='Pre-registration list',
            status_code=status.HTTP_200_OK
        )


class SearchPreRegistrationAPIView(generics.ListAPIView):
    serializer_class = PreRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return PreRegistration.objects.filter(email=self.kwargs['email'])

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if not serializer.data:
            return ResponseHelper.warning_response(
                message='Pre-registration not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        else:
            return ResponseHelper.success_response(
                data=serializer.data,
                message='Pre-registration found',
                status_code=status.HTTP_200_OK
            )


class CreatePreRegistrationAPIView(generics.ListCreateAPIView):
    """
    Crea un preregistro y envia un email
    """
    serializer_class = PreRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return PreRegistration.objects.all()

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    self.perform_create(serializer)
                    # EmailHelper.send(
                    #     destinatario=serializer.data.get('email'),
                    #     asunto='Pre-registro Animal Force',
                    #     template_path='emails/pre-register.html',
                    #     context=serializer.data
                    # )
                    return ResponseHelper.success_response(
                        data=serializer.data,
                        message='Pre-registration was successful',
                        status_code=status.HTTP_201_CREATED
                    )
            except Exception as e:
                return ResponseHelper.transaction_error_response(
                    exception=e,
                    message='An error occurred while registering the pre-registration.',
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return ResponseHelper.error_response(
                errors=serializer.errors,
                message='Ocurrio un error al registrar',
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )


class DestroyPreregistrationApiView(generics.DestroyAPIView):
    """
    Elimina un preregistro
    """
    serializer_class = PreRegistrationSerializer
    permission_classes = [permissions.IsAdminUser]