from django.urls import path

from . import views

urlpatterns = [
    path('get-user/', views.provide_user_info_partial, name='get_user'),
    path('', views.index, name='index')
]