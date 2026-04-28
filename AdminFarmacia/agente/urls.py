from django import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agentes/', views.lista_agentes, name='listaAgentes'),
]
