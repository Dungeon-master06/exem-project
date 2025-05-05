from django.shortcuts import render
from .models import Settings, FAQ, SocialLink
from django.contrib.auth.models import User


def home(request):
    settings = Settings.objects.latest('id')
    social_links = SocialLink.objects.all()
    context = {
        'settings': settings,
        'social_links': social_links,
        'total_users': User.objects.count()
    }
    return render(request, 'index.html', context)


def contact(request):
    settings = Settings.objects.latest('id')
    social_links = SocialLink.objects.all()
    context = {
        'settings': settings,
        'social_links': social_links,
    }
    return render(request, 'pages/contact.html', context)


def faq(request):
    settings = Settings.objects.latest('id')
    faqs = FAQ.objects.all()
    social_links = SocialLink.objects.all()
    context = {
        'settings': settings,
        'faqs': faqs,
        'social_links': social_links
    }
    return render(request, 'pages/faq.html', context)


def social_links(request):
    return {
        'social_links': SocialLink.objects.all()
    }