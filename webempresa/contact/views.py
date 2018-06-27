from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage 
from .forms import ContacForm
# Create your views here.

def contact(request):
    contact_form = ContacForm()

    if request.method == "POST":
        contact_form = ContacForm(data=request.POST)
        if contact_form.is_valid(): 
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y Redericcionamos
            email = EmailMessage(
                "La Caffetera: Nuevo mensaje de Correo",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "rodrigo.rivera@cfe.mx",
                ["rrivera451@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #Todo salio Bien y  y redericcionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo fallo no salio bien y redericcionamos a FAIL
                 return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
