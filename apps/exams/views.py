from django.shortcuts import render
from .models import Settings

def home(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings
    }
    return render(request, 'index.html', context)

def contact(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings
    }
    return render(request, 'pages/contact.html', context)

def faq(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings
    }
    return render(request, 'pages/faq.html', context)
