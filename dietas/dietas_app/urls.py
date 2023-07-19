from django.urls import path
from .views import index,processar_formulario, login, logout

urlpatterns = [
    path('index', index, name='index'),
    path('processar_formulario', processar_formulario, name='processar_formulario'),
    path('', login , name='login'),
    path('logout/', logout , name='logout'),
]
