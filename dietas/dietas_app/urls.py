from django.urls import path
from .views import index,processar_formulario

urlpatterns = [
    path('', index, name='index'),
    path('processar_formulario', processar_formulario, name='processar_formulario'),
]
