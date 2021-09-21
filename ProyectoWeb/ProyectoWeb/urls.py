from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('servicios/', include('ServiciosApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('', include('ProyectoWebApp.urls')),
]
