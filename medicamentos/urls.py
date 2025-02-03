from django.urls import path
from . import views

urlpatterns = [
    path('medicamentos', views.medicamentos, name='medicamentos')
]
