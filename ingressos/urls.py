from django.urls import path

from ingressos.views import home, logout, login

app_name = 'ingressos'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', login, name='login'),
    path('accounts/logout', logout, name='logout'),
]
