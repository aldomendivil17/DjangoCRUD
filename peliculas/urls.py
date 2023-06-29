from django.urls import path
from .views import agregar_pelicula, lista_peliculas, eliminar_pelicula, actualizar_pelicula, get_pelicula_id, cancelar, agregar_screen

app_name = 'peliculas'

urlpatterns  = [
    path('',lista_peliculas, name="lista_peliculas"),
    path('new/', agregar_pelicula, name="agregar_pelicula"),
    path('eliminar_pelicula/<int:id_pelicula>/', eliminar_pelicula, name='eliminar_pelicula'),
    path('editar_pelicula/<int:id_pelicula>/', get_pelicula_id, name='get_pelicula'),
    path('actualizar_pelicula/<int:id_pelicula>/', actualizar_pelicula, name='actualizar_pelicula'),
    path('', cancelar, name="cancelar"),
    path('agregar_screen/', agregar_screen, name="agregar_screen"),
]
