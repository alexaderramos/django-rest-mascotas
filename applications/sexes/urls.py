from django.urls import path
from .views import (
    SexListApiView,
    SexCreateApiView,
    SexRetrieveApiView,
    SexUpdateApiView,
    SexDestroyApiView
)

urlpatterns = [
    path('list', SexListApiView.as_view()),
    path('create', SexCreateApiView.as_view()),
    path('detail/<int:pk>', SexRetrieveApiView.as_view()),
    path('update/<int:pk>', SexUpdateApiView.as_view()),
    path('delete/<int:pk>', SexDestroyApiView.as_view()),
]
