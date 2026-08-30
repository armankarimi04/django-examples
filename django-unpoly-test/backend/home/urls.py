from django.urls import path

from . import views

urlpatterns = [
    path("article/<int:pk>/", views.get_article, name='get-article'),
    path("", views.index, name='index'),
]