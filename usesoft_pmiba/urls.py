from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    
    # User Management
    path('users', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]
urlpatterns += i18n_patterns(
    path('', include('ingressos.urls')), prefix_default_language=True
)
