from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from astro_shop.settings import EMAIL_HOST_USER

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']    
            return_info = "Thank you for your message, we will get back to you soon."   
            pass_to_me_message = "Message from: " + from_email + "\n" + "Message: \n" + message
            try:
                send_mail(subject, return_info, EMAIL_HOST_USER, [from_email])
                send_mail(subject, pass_to_me_message, EMAIL_HOST_USER, ['astronomyproject28@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponseRedirect('success')