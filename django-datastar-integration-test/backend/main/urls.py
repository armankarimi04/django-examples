from django.urls import path

from . import views

urlpatterns = [
    path('provide-films/', views.provide_films, name='provide_films'),
    path('new-film-form-submit/', views.new_film, name='new_film_submit'),
    path('provide-new-film-form/', views.provide_new_film_form, name='provide_new_film_form'),
    path('films/', views.index, name='index'),
]