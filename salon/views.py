from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

from config.settings import EMAIL_HOST_USER
from .models import Service, Price, Photos, Style1


# Create your views here.
def index(request):
    return render(request, 'index.html', )


def about(request):
    return render(request, 'about.html')


def service(request):
    serves = Service.objects.all()

    return render(request, 'service.html', {'serves': serves})


def price(request):
    prices = Price.objects.all()

    return render(request, 'price.html', {'prices': prices})


def portfolio(request):
    photos = Photos.objects.all()

    return render(request, 'portfolio.html', {'photos': photos}, )


def style1(request):
    styles1 = Style1.objects.all()

    return render(request, 'portfolio.html', {'styles1': styles1})


def contact(request):
    message = request.POST.get('message', '')
    subject = request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
    email.content_subtype = 'html'
    email.send()
    # return HttpResponse("sent")

    return render(request, 'contact.html')
