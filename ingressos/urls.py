from django.urls import path

from ingressos.views import home, logout, login, EventoCreate

app_name = 'ingressos'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login', login, name='login'),
    path('accounts/logout', logout, name='logout'),
    
    path('evento_add', EventoCreate.as_view(), name='evento_add'),
]
