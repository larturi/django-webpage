from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('ServiciosApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contacto/', include('ContactoApp.urls')),
    path('tienda/', include('TiendaApp.urls')),
    path('carrito/', include('CarritoApp.urls')),
    path('', include('ProyectoWebApp.urls')),
]
