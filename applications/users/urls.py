# from django.contrib import admin
# from django.urls import path
#
# from applications.users import views
#
# urlpatterns = [
#     # api
#     path('users/', views.UserListApiView.as_view()),
#     path('users/search/<kword>', views.UserSearchApiView.as_view())
#
# ]


from django.urls import path

from . import views

urlpatterns = [
    # path('', include(router.urls)),

    path('list', views.UserListApiView.as_view()),
    path('search/<kword>', views.UserSearchApiView.as_view()),
    path('create', views.UserCreateApiView.as_view()),
    path('update/<pk>', views.UserUpdateApiView.as_view()),
    path('delete/<pk>', views.UserDeleteApiView.as_view()),
    path('detail/<int:pk>', views.UserRetrieveApiView.as_view()),
    path('clients', views.UserClientListApiView.as_view())

]
