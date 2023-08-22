from django.urls import path
from .views import (
    PetListApiView,
    PetCreateApiView,
    PetRetrieveApiView,
    PetUpdateApiView,
    PetDestroyApiView,
    #
    PetListByParentView,
    PetSiblingsListView,
    PetListByOwnerView,
    PetChildrenByParentView,
    #
    PetVaccineListByPetView,
    #
    PetVaccineCreateApiView,
    PetVaccineDestroyApiView,
)

urlpatterns = [
    path('list/', PetListApiView.as_view()),
    path('create/', PetCreateApiView.as_view()),
    path('detail/<int:pk>', PetRetrieveApiView.as_view()),
    path('update/<int:pk>', PetUpdateApiView.as_view()),
    path('delete/<int:pk>', PetDestroyApiView.as_view()),
    #
    path('detail/<int:pet_id>/vaccines/', PetVaccineListByPetView.as_view()),
    path('detail/<int:pet_id>/childrens/', PetListByParentView.as_view()),
    path('detail/<int:pet_id>/siblings/', PetSiblingsListView.as_view()),

    path('parents/<int:father_id>/<int:mother_id>/children/', PetChildrenByParentView.as_view()),

    path('owners/<int:owner_id>/pets/', PetListByOwnerView.as_view()),

    #

    path('pet-vaccines/create/', PetVaccineCreateApiView.as_view(), ),
    path('pet-vaccines/delete/<int:pk>', PetVaccineDestroyApiView.as_view()),

]
