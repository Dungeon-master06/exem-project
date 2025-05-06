from django.shortcuts import render
from .models import Settings, FAQ, SocialLink
from django.contrib.auth.models import User
from apps.exams.models import Test


def home(request):
    settings = Settings.objects.order_by('-id').first() 
    social_links = SocialLink.objects.all()
    tests = Test.objects.all()
    recent_tests = Test.objects.order_by('-created_at')[:3]
    context = {
        'settings': settings,
        'social_links': social_links,
        'tests': tests,
        'recent_tests':recent_tests,
        'total_users': User.objects.count(),
        'total_tests': Test.objects.count(),
    }
    return render(request, 'index.html', context)


def contact(request):
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    context = {
        'settings': settings,
        'social_links': social_links,
    }
    return render(request, 'pages/contact.html', context)


def faq(request):
    settings = Settings.objects.order_by('-id').first()
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