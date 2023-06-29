from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

# Create your views here.


@login_required
def actualizarUser_screen(request):
    return render(request, 'user.html')

@login_required
def actualizarUsuario(request):
     if request.method == 'POST':
        new_username = request.POST.get('new_username')
        print(new_username)
        user = request.user

        if new_username:
            user.username = new_username
            user.save()
            messages.success(request,"Se modificó el nombre de usuario correctamente", extra_tags='correcto')
            url = reverse('usuarios:actualizarUser_screen')
            return redirect(url)
        else :
            messages.success(request,"No se pudo modificar el nombre de usuario correctamente", extra_tags='error')
            url = reverse('usuarios:actualizarUser_screen')
            return redirect(url)

@login_required
def actualizarContraseña(request):
    if request.method == 'POST':
        actualContraseña = request.POST.get('actualContraseña')
        nuevaContraseña = request.POST.get('nuevaContraseña')
        confirmacionNuevaContraseña = request.POST.get('confirmacionNuevaContraseña')
        usuario = request.user

        if check_password(actualContraseña, usuario.password):
            if nuevaContraseña == confirmacionNuevaContraseña:
                if check_password(nuevaContraseña, usuario.password):
                    messages.success(request,"No se realizó ningún cambio. La contraseña actual y nueva son iguales", extra_tags='error')
                    url = reverse('usuarios:actualizarUser_screen')
                    return redirect(url)
                else:
                    usuario.set_password(nuevaContraseña)
                    usuario.save()
                    update_session_auth_hash(request, usuario)
                    messages.success(request,"Se modificó la contraseña correctamente", extra_tags='correcto')
                    url = reverse('usuarios:actualizarUser_screen')
                    return redirect(url)
            else:
                messages.success(request,"Las contraseñas no coinciden. Intenta otra vez", extra_tags='error')
                url = reverse('usuarios:actualizarUser_screen')
                return redirect(url)
        else:
            messages.success(request,"La contraseña actual es incorrecta. Intenta otra vez", extra_tags='error')
            url = reverse('usuarios:actualizarUser_screen')
            return redirect(url)    


@login_required
def cambiarImagen(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if image_file:
            print('Hola')
            request.user.picture = image_file
            request.user.save()
            messages.success(request,"Se cambió la imagen de perfil correctamente", extra_tags='correcto')
            url = reverse('usuarios:actualizarUser_screen')
            return redirect(url)
        else:
            messages.success(request,"No se pudo cambiar la imagen de perfil correctamente. Intenta otra vez", extra_tags='error')
            url = reverse('usuarios:actualizarUser_screen')
            return redirect(url)
    