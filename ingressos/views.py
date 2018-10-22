from django.shortcuts import render


def home(request):
    idioma = 'Idioma: '
    return render(request, 'ingressos/home.html', {'idioma': idioma})


def login(request):
    return render(request, 'account/login.html', {})


def logout(request):
    return render(request, 'account/logout.html', {})
