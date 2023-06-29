from django.urls import path
from .views import lista_generos, crear_genero, eliminar_genero, get_genero_id, cancelar_editGen, actualizar_genero, agregar_genero

from . import views

app_name = 'generos'

urlpatterns = [
    path('',lista_generos, name="lista_generos"),
    path('new/', crear_genero, name='crear_genero'),
    path('eliminar_genero/<int:id_genero>/', eliminar_genero, name='eliminar_genero'),
    path('editar_genero/<int:id_genero>/', get_genero_id, name='get_genero'),
    path('actualizar_genero/<int:id_genero>/', actualizar_genero, name='actualizar_genero'),
    path('generos/', cancelar_editGen, name="cancelar_editGen"),
    path('agregar_genero/', agregar_genero, name="agregar_genero"),
    

]