from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio/", views.inicio, name="inicio"),
    path("remito/lista_remito/", views.lista_remito, name="lista_remito"),
    path("remito/alta_remito/", views.alta_remito, name="alta_remito"),
    path(
        "remito/modificacion_remito/<int:id_remito>/",
        views.modificacion_remito,
        name="modificacion_remito",
    ),
    path(
        "remito/eliminacion_remito/<int:id_remito>/",
        views.eliminacion_remito,
        name="eliminacion_remito",
    ),
    path(
        "remito/imprimir_remito/<int:id_remito>/",
        views.imprimir_remito,
        name="imprimir_remito",
    ),
]
