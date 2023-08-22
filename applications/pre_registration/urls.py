from django.urls import path

from .views import CreatePreRegistrationAPIView, ListPreRegistrationAPIView, SearchPreRegistrationAPIView, DestroyPreregistrationApiView

urlpatterns = [
    path('save', CreatePreRegistrationAPIView.as_view(), name='pre-registration-create'),
    path('list', ListPreRegistrationAPIView.as_view(), name='pre-registration-list'),
    path('search/<str:email>', SearchPreRegistrationAPIView.as_view(), name='pre-registration-search'),
    path('delete/<int:pk>', DestroyPreregistrationApiView.as_view(), name='pre-registration-delete'),

]
