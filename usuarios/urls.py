from django.urls import path
from .views import actualizarUser_screen, actualizarUsuario, actualizarContraseña, cambiarImagen


app_name = 'usuarios'

urlpatterns  = [
    path('actualizarUser_screen/',actualizarUser_screen , name="actualizarUser_screen"),
    path('actualizarUsuario/', actualizarUsuario, name="actualizarUsuario"),
    path('actualizarContraseña/', actualizarContraseña, name="actualizarContraseña"),
    path('cambiarImagen/', cambiarImagen, name="cambiarImagen"),
]