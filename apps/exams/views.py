from django.shortcuts import render
from .models import Settings, FAQ
from django.contrib.auth.models import User

def home(request):
    settings = Settings.objects.latest('id')
    context = {
        'settings': settings,
        'total_users': User.objects.count()
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
    faqs = FAQ.objects.all()
    context = {
        'settings': settings,
        'faqs': faqs
    }
    return render(request, 'pages/faq.html', context)
