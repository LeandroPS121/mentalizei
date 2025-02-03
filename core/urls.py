from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  
    path('medicamentos/', include('medicamentos.urls')), 
    path('home/', include('home.urls')),  
    
    path('', lambda request: redirect('home')),
]