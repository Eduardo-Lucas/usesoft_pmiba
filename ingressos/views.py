from django.shortcuts import render
from django.utils.translation import gettext as _


def home(request):
    output = _("Bem-vindo.")
    return render(request, 'ingressos/home.html', {'output': output})
