from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Pelicula
from generos.models import Genero 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cancelar(request):
    return render(request, 'agregar_pelicula.html')

@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'lista_peliculas.html', {'peliculas': peliculas, "generos":Genero.objects.all() })

@login_required
def agregar_screen(request):
    return render(request, 'agregar_pelicula.html', {"generos":Genero.objects.all() })

@login_required
def agregar_pelicula(request):
    if request.method == "POST":
        generos = request.POST.getlist("genero")
        print(generos)
        pelicula = Pelicula(titulo=request.POST['titulo'], anhio = request.POST['anhio'], director = request.POST['director'])
        pelicula.save()

        pelicula.generos.set(generos)
        messages.success(request,"Se agregó la pelicula "+"'"+pelicula.titulo+"'"+" correctamente", extra_tags='correcto')
        return redirect('/peliculas/')
    else:
        return render(request,"agregar_pelicula.html",{"generos":Genero.objects.all()})

@login_required
def eliminar_pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    pelicula.delete()
    messages.success(request,"Se eliminó la pelicula "+"'"+pelicula.titulo+"'"+" correctamente", extra_tags='correcto')
    return redirect('/peliculas/')

@login_required
def get_pelicula_id(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    return render(request, 'editar_pelicula.html', {"pelicula_obj": pelicula, "generos":Genero.objects.all()})

@login_required
def actualizar_pelicula(request, id_pelicula):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        anhio = request.POST.get('anhio')
        director = request.POST.get('director')
        generos = request.POST.getlist("genero")

    pelicula = Pelicula(
        id = id_pelicula,
        titulo =  titulo,
        anhio =  anhio,
        director = director,
    )

    pelicula.save()
    pelicula.generos.set(generos)
    messages.success(request,"Se modificó la pelicula "+"'"+pelicula.titulo+"'"+" correctamente", extra_tags='correcto')
    url = reverse('peliculas:get_pelicula', args=[id_pelicula])
    return redirect(url)
