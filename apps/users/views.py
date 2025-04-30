from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout, get_user_model
from apps.exams.models import Settings
User = get_user_model()


def login_view(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        usr = authenticate(request, username=login, password=password)
        if usr is not None: # проверка на сущ
            user_login(request, usr)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/login.html', {'error':'Неверный логин или пароль' })
    return render(request, 'accounts/login.html', {'settings':settings})


def reg_view(request):
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'accounts/register.html', {'error':'Пароли не совпадают'})
        if len(password)< 6:
            return render(request, 'accounts/register.html', {'error':'Пароль должен быть больше 6 символов'})
        if password == password2:
            User.objects.create_user(username=login, password=password)
            usr = authenticate(request, username=login, password=password)
            if usr is not None: # проверка на сущ
                user_login(request, usr)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'accounts/register.html', {'error':'Неверный логин или пароль',})
    return render(request, 'accounts/register.html', {'settings':settings})


def logout_view(request):
    user_logout(request)
    return HttpResponseRedirect('/')


