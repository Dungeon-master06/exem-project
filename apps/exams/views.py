from django.shortcuts import render
from .models import Settings

def home(request):
    settings = Settings.objects.all()
    contex = {
        'settings': settings
    }
    return render(request, 'index.html', contex)

def contact(request):
    settings = Settings.objects.all()
    contex = {
        'settings': settings
    }
    return render(request, 'pages/contact.html', contex)

def faq(request):
    return render(request, 'pages/faq.html')
