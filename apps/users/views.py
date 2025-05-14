from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, get_user_model
from apps.settingis.models import Settings, SocialLink
User = get_user_model()


def login_view(request):
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        usr = authenticate(request, username=login, password=password)
        if usr is not None: # проверка на сущ
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/accounts/login.html', {'error':'Неверный логин или пароль' ,'settings':settings, 'social_links':social_links})
    return render(request, 'pages/accounts/login.html', {'settings':settings, 'social_links':social_links})


def reg_view(request):
    settings = Settings.objects.order_by('-id').first()
    social_links = SocialLink.objects.all()
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'pages/accounts/register.html', {'error':'Пароли не совпадают','settings':settings, 'social_links':social_links})
        if len(password)< 6:
            return render(request, 'pages/accounts/register.html', {'error':'Пароль должен быть больше 6 символов','settings':settings, 'social_links':social_links})
        if password == password2:
            User.objects.create_user(username=login, password=password)
            usr = authenticate(request, username=login, password=password)
            if usr is not None: # проверка на сущ
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'pages/accounts/register.html', {'error':'Неверный логин или пароль','settings':settings, 'social_links':social_links})
    return render(request, 'pages/accounts/register.html', {'settings':settings, 'social_links':social_links})


def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')