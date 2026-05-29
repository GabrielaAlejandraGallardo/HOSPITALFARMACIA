from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('medicamento/lista_medicamento/', views.lista_medicamento, name='lista_medicamento'),
    path('medicamento/alta_medicamento/',views.alta_medicamento,name='alta_medicamento'),
    path('medicamento/eliminacion_medicamento/<int:id_medicamento>/',views.eliminacion_medicamento,name='eliminacion_medicamento'),
    path('medicamento/modificaciones_medicamento/<int:id_medicamento>/',views.modificaciones_medicamento,name='modificaciones_medicamento'),
    path('medicamento/lista_laboratorio/', views.lista_laboratorio, name='lista_laboratorio'),
    path('medicamento/alta_laboratorio/',views.alta_laboratorio,name='alta_laboratorio'),
    path('medicamento/eliminacion_laboratorio/<int:id_laboratorio>/',views.eliminacion_laboratorio,name='eliminacion_laboratorio'),
    path('medicamento/modificaciones_laboratorio/<int:id_laboratorio>/', views.modificaciones_laboratorio,name='modificaciones_laboratorio'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)