from django.shortcuts import render, redirect
from .carrito import Carrito
from TiendaApp.models import Producto

def carrito(request):
    return render(request, "CarritoApp/carrito.html")

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregarProducto(producto=producto)
    return redirect("/carrito/show")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminarProducto(producto=producto)
    return redirect("/carrito/show")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restarCantidadProducto(producto=producto)
    return redirect("/carrito/show")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.vaciarCarrito()
    return redirect("tienda")
