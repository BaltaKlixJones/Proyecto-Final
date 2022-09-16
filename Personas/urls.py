from django import views
from django.urls import path
from Personas.views import *




urlpatterns = [
    path('', inicio, name="Inicio"),
    path('campeones/', campeones, name="Campeones"),
    path('nosotros', nosotros, name="Contacto"),
    path('persona', persona, name="Persona"),
    path('buscar', buscar, name="buscar"),
    path('buscaNombre', buscaNombre, name="buscaNombre"),
    path('buscaPais', buscaPais, name="buscaPais"),
    path('BuscartorneoY', buscarTorneoY, name="buscarTorneoY"),
    path('BuscartorneoN', buscarTorneoN, name="buscarTorneoN"),
    path('BuscartorneoJ', buscarTorneoJ, name="buscarTorneoJ"),
    path('torneo', torneo, name="Torneo"),
    path('leerpersonas/', leerPersonas , name="leerPersonas"),
    path('elminarPersona/<id>', eliminarPersonas , name="eliminarPersonas"),
    path('editarPersona/<id>', editarPersonas , name="editarPersona"),
]