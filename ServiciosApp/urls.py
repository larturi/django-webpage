from django.urls import path

from ServiciosApp import views

urlpatterns = [
    path('', views.servicios, name="servicios"),
]

