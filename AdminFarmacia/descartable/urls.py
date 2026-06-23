
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('descartable/lista_descartable/', views.lista_descartable, name='lista_descartable'),
<<<<<<< HEAD
    path('descartable/alta_descartable/',views.alta_descartable,name='alta_descartable'),
    path('descartable/eliminacion_descartable/<int:id_descartable>/',views.eliminacion_descartable,name='eliminacion_descartable'),
    path('descartable/modificaciones_descartable/<int:id_descartable>/',views.modificaciones_descartable,name='modificaciones_descartable'),
    path('descartable/lista_laboratorio/', views.lista_laboratorio, name='lista_laboratorio'),
    path('descartable/alta_laboratorio/',views.alta_laboratorio,name='alta_laboratorio'),
    path('descartable/eliminacion_laboratorio/<int:id_laboratorio>/',views.eliminacion_laboratorio,name='eliminacion_laboratorio'),
    path('descartable/modificaciones_laboratorio/<int:id_laboratorio>/', views.modificaciones_laboratorio,name='modificaciones_laboratorio'),
    path('descartable/<int:id_descartable>/', views.realizar_dispensa, name='dispensa_medicamento'),
    path('mas-dispensados/', views.medicamentos_mas_dispensados, name='medicamentos_mas_dispensados'),
    path('reporte-diario/', views.reporte_diario, name='reporte_diario'),
    path("buscar/", views.buscar_descartable, name="buscar_descartable"),
=======
    path('descartable/alta_descartable/', views.alta_descartable, name='alta_descartable'),
    path('descartable/eliminacion_descartable/<int:id_descartable>/', views.eliminacion_descartable, name='eliminacion_descartable'),
    path('descartable/modificaciones_descartable/<int:id_descartable>/', views.modificaciones_descartable, name='modificaciones_descartable'),
    path('descartable/lista_laboratorio/', views.lista_laboratorio, name='lista_laboratorio'),
    path('descartable/alta_laboratorio/', views.alta_laboratorio, name='alta_laboratorio'),
    path('descartable/eliminacion_laboratorio/<int:id_laboratorio>/',views.eliminacion_laboratorio,name='eliminacion_laboratorio'),
    path('descartable/modificaciones_laboratorio/<int:id_laboratorio>/', views.modificaciones_laboratorio,name='modificaciones_laboratorio'),
    path('dispensa/<int:id_medicamento>/', views.realizar_dispensa, name='dispensa_medicamento'),
    path('mas-dispensados/', views.descartable_mas_dispensados, name='descartable_mas_dispensados'),
    path('reporte-diario/', views.reporte_diario, name='reporte_diario'),
>>>>>>> 3506bcb9958dee91c886cb7c09d97d3b0e703b89
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)