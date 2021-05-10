from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email_form = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # As everything goes well, we send an email.
            email = EmailMessage(
                "La Caffetiera: Nuevo Mensaje de Contacto",  # Subject
                f"De {name} <{email_form}>\n\nEscribio:\n\n{content}",  # Body message
                "no-contestar@inbox.mailtrap.io",  # email from
                [email_form],  # email to
                reply_to=[email_form]  # if this email is an answer from another one
            )
            try:
                email.send()
            except:
                print("------------------------------")
                print("NEFASTOO!!")
                print("------------------------------")
            return redirect(reverse('contact') + '?ok')

    return render(request, "contact/contact.html", {"form": contact_form})
