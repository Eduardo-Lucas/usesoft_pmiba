from django.shortcuts import render


def home(request):
    idioma = 'Idioma: '
    return render(request, 'ingressos/home.html', {'idioma': idioma})
