from django.urls import path
from .views import modificarUsuario, actualizarUser_screen

app_name = 'usuarios'

urlpatterns  = [
    path('modificarUsuario/', modificarUsuario, name="modificarUsuario"),
    path('actualizarUser_screen/',actualizarUser_screen , name="actualizarUser_screen"),
    #path('actualizarUsuario/', actualizarUsuario, name="actualizarUsuario"),
    #path('actualizarContraseña/', actualizarContraseña, name="actualizarContraseña"),
    #path('cambiarImagen/', cambiarImagen, name="cambiarImagen"),
]