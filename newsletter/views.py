from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# random num for confirmation number
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

@csrf_exempt   # disables csrf protection for this view
def new(request):
    if request.method == 'POST':
        mail = request.POST['email']
        if "@" in mail:         # error warning for @ missing
            sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
            if Subscriber.objects.filter(email = mail).exists():   # catching integrity error from duplicate email added
                return render(request, 'newsletter.html', {'email': sub.email, 'action': 'registered previously', 'form': SubscriberForm()})
            else:
                sub.save()
                message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject='Newsletter Confirmation',
                    html_content='Thank you for signing up for our Astronomy Shop email newsletter! \
                        Please complete the process by \
                        <a href="{}?email={}&conf_num={}"> clicking here to \
                        confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)   # uses sendgrid system
                response = sg.send(message)
                return render(request, 'newsletter.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
        else:
            return render(request, 'newsletter.html', {'email': mail, 'action': 'is not a valid address, please try again', 'form': SubscriberForm()})
    else:
            return render(request, 'newsletter.html', {'form': SubscriberForm()})


def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'newsletter.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'newsletter.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'newsletter.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'newsletter.html', {'email': sub.email, 'action': 'denied'})

def terms(request):
    return render(request, 'terms.html')