from django.urls import path
from .views import (
    VaccineListApiView,
    VaccineCreateApiView,
    VaccineRetrieveApiView,
    VaccineUpdateApiView,
    VaccineDestroyApiView,
)

urlpatterns = [
    path('list/', VaccineListApiView.as_view(), name='vaccine-list-create'),
    path('create/', VaccineCreateApiView.as_view(), name='vaccine-list-create'),
    path('detail/<int:pk>/', VaccineRetrieveApiView.as_view(), name='vaccine-retrieve'),
    path('update/<int:pk>/', VaccineUpdateApiView.as_view(), name='vaccine-update'),
    path('delete/<int:pk>/', VaccineDestroyApiView.as_view(), name='vaccine-delete'),
]
