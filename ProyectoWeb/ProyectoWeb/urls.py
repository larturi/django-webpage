from django.contrib import admin
from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('servicios', views.servicios, name="Servicios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
]
