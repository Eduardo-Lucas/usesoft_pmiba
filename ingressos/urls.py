from django.urls import path

from ingressos.views import home

urlpatterns = [
    path('', home, name='home'),
]
