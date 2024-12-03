from django.urls import path
from trocas_app import views

urlpatterns = [
    path("trocas", views.inicio_vistaTrocas, name="trocas"),
    path("registrarTroca/", views.registrarTroca, name="registrarTroca"),
    path("seleccionarTroca/<codigo>", views.seleccionarTroca, name="seleccionarTroca"),
    path("editarTroca/", views.editarTroca, name="editarTroca"),
    path("borrarTroca/<codigo>", views.borrarTroca, name="borrarTroca"),
]
