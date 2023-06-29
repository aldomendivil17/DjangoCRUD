from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

def log(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('peliculas:lista_peliculas'))
    else:
        return render(request, './templates/login.html')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('log'))

def login_view(request):
    if request.user.is_authenticated:
        nombre_imagen = request.user.first_name
        url = reverse('peliculas:lista_peliculas') + f'?imagen={nombre_imagen}'
        return HttpResponseRedirect(url)
 
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('peliculas:lista_peliculas'))
    else:
        messages.success(request,"Usuario y/o contraseña incorrecta. Intenta de nuevo." , extra_tags='error')
        return render(request, './templates/login.html', {'error': 'Credenciales inválidas'})
    
    