from django.urls import path

from .views import (
    ListSpecieApiView,
    CreateSpecieApiView,
    UpdateSpecieApiView,
    DeleteSpecieApiView,
    SpecieRetrieveApiView
)

urlpatterns = [
    path('list/', ListSpecieApiView.as_view()),
    path('create/', CreateSpecieApiView.as_view()),
    path('detail/<pk>', SpecieRetrieveApiView.as_view()),
    path('update/<pk>', UpdateSpecieApiView.as_view()),
    path('delete/<pk>', DeleteSpecieApiView.as_view()),

]
