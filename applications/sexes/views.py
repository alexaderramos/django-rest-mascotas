# Create your views here.


from rest_framework import generics, permissions, status

from utils.helpers import ResponseHelper
from .models import Sex
from .serializers import SexSerializer


class SexListApiView(generics.ListAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        return ResponseHelper.success_response(
            data=serializer.data,
            message='Sex list',
            status_code=200
        )


class SexCreateApiView(generics.CreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
    permission_classes = [permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseHelper.success_response(
                data=serializer.data,
                message='Specie created successfully',
                status_code=status.HTTP_201_CREATED
            )
        else:
            return ResponseHelper.error_response(
                errors=serializer.errors,
                message='Specie not created',
                status_code=status.HTTP_400_BAD_REQUEST
            )


class SexRetrieveApiView(generics.RetrieveAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        if not serializer.data:
            return ResponseHelper.error_response(
                errors=serializer.errors,
                message='Specie not found',
                status_code=status.HTTP_404_NOT_FOUND
            )
        else:

            return ResponseHelper.success_response(
                data=serializer.data,
                message='Specie retrieved successfully',
                status_code=status.HTTP_200_OK
            )


class SexUpdateApiView(generics.UpdateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return ResponseHelper.success_response(
                data=serializer.data,
                message='Specie updated successfully',
                status_code=status.HTTP_200_OK
            )
        else:
            return ResponseHelper.error_response(
                errors=serializer.errors,
                message='Specie not updated',
                status_code=status.HTTP_400_BAD_REQUEST
            )


class SexDestroyApiView(generics.DestroyAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer
