from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio/", views.inicio, name="inicio"),

    path("descartable/lista_descartable/", views.lista_descartable, name="lista_descartable"),
    path("descartable/alta_descartable/", views.alta_descartable, name="alta_descartable"),
    path(
        "descartable/eliminacion_descartable/<int:id_descartable>/",
        views.eliminacion_descartable,
        name="eliminacion_descartable",
    ),
    path(
        "descartable/modificaciones_descartable/<int:id_descartable>/",
        views.modificaciones_descartable,
        name="modificaciones_descartable",
    ),

    # Laboratorios/huecos/supervisores aún no están implementados de forma consistente.
    # Rutas temporales eliminadas para evitar AttributeError durante el arranque.


    path("descartable/realizar_dispensa/<int:id_descartable>/", views.realizar_dispensa, name="realizar_dispensa"),
    path("descartable/descartable_mas-dispensados/", views.descartable_mas_dispensados, name="descartable_mas_dispensados"),
    path("descartable/reporte-diario/", views.reporte_diario, name="reporte_diario"),

    path("descartable/buscar/", views.buscar_descartable, name="buscar_descartable"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

