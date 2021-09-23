from django.shortcuts import render, redirect

from .forms import FormContacto

def contacto(request):

    formulario_contacto = FormContacto()

    if request.method == "POST":

        formulario_contacto = FormContacto(data=request.POST)

        if formulario_contacto.is_valid():

            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            return redirect("/contacto/?valid")

    return render(request, "ContactoApp/contacto.html", {'formulario_contacto': formulario_contacto})
