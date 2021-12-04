"""Home app views"""
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """View for contact us form"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Brainworks website Enquiry"
            body = {
                'message': form.cleaned_data['message'],
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email_address']
            }
            message = "\n".join(body.values())
            messages.success(request, 'Message sent successfully!')

            try:
                send_mail(subject, message, 'brainworks.33@gmail.com', [
                    'brainworks.33@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            messages.error(
                request, "Form not submitted. Please correct any errors")
            return render(request, 'contact.html', {'form': form})
    form = ContactForm()
    return render(request, "contact/contact.html", {'form': form}, {'on_profile_page': True})
