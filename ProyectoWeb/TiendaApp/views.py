from django.shortcuts import render

from .models import Producto

def tienda(request):

    productos = Producto.objects.all()

    return render(request, "TiendaApp/tienda.html", {"productos": productos})
