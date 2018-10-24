from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView

from ingressos.models import Evento


def home(request):
    idioma = 'Idioma: '
    return render(request, 'ingressos/home.html', {'idioma': idioma})


def login(request):
    return render(request, 'account/login.html', {})


def logout(request):
    return render(request, 'account/logout.html', {})


class EventoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Evento
    fields = '__all__'
    template_name = 'ingressos/evento/evento_form.html'
