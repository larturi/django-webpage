from django.shortcuts import render, redirect

from .forms import FormContacto

from django.core.mail import EmailMessage

import traceback

def contacto(request):

    formulario_contacto = FormContacto()

    if request.method == "POST":

        formulario_contacto = FormContacto(data=request.POST)

        if formulario_contacto.is_valid():

            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            emailSend = EmailMessage(
                "Mensaje desde App de Django", "El usuario con nombre {} y correo {} escribe lo siguiente:\n\n {}".format(nombre, email, mensaje), 
                "", 
                ["lea.arturi.drive@gmail.com"],
                reply_to=[email])

            try:
                emailSend.send()
                return redirect("/contacto/?valid")

            except Exception as e:
                trace_back = traceback.format_exc()
                message = str(e)+ " " + str(trace_back)
                print (message)
                return redirect("/contacto/?novalid")

    return render(request, "ContactoApp/contacto.html", {'formulario_contacto': formulario_contacto})
