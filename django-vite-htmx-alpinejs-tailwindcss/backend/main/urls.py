from django.urls import path

from . import views
app_name = "main"
urlpatterns = [
    path('htmx-test/', views.htmx_test, name='htmx_test'),
    path('test-page/', views.test_page),
    path('', views.index, name='index')   
]