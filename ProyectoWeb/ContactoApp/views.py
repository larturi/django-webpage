from django.shortcuts import render

from .forms import FormContacto

def contacto(request):

    formulario_contacto = FormContacto()

    return render(request, "ContactoApp/contacto.html", {'formulario_contacto': formulario_contacto})
