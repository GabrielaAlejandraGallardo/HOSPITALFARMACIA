
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('lista_agentes/', views.lista_agentes, name='lista_agentes'),
    path('alta_agentes/',views.alta_agentes,name='alta_agentes'),
    path('eliminacion_agentes/<int:id_agente>/',views.eliminacion_agentes,name='eliminacion_agentes'),
    # alias para compatibilidad con template antiguo
    path('eliminacion_agentes/<int:id_agente>/',views.eliminacion_agentes,name='eliminacion_agente'),
    path('modificacion_agentes/<int:id_agente>/',views.modificacion_agentes,name='modificacion_agentes'),
    # Compatibilidad con enlaces existentes que usan prefijo "agentes/"
    path('agentes/lista_agentes/', views.lista_agentes, name='lista_agentes'),
    path('agentes/alta_agentes/', views.alta_agentes, name='alta_agentes'),
    path('agentes/eliminacion_agentes/<int:id_agente>/', views.eliminacion_agentes, name='eliminacion_agentes'),
    path('agentes/modificacion_agentes/<int:id_agente>/', views.modificacion_agentes, name='modificacion_agentes')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
