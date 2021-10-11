from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('ServiciosApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contacto/', include('ContactoApp.urls')),
    path('tienda/', include('TiendaApp.urls')),
    path('carrito/', include('CarritoApp.urls')),
    path('', include('ProyectoWebApp.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
