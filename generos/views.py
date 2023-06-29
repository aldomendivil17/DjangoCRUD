from django.shortcuts import render, redirect
from .models import Genero
from peliculas.views import Pelicula
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cancelar_editGen(request):
    generos = Genero.objects.all()
    return render(request, 'lista_generos.html', {'generos': generos})

# views para abrir nuevas ventanas

@login_required
def lista_generos(request):
        generos = Genero.objects.all()
        return render(request, 'lista_generos.html', {'generos': generos})

@login_required
def agregar_genero(request):
    return render(request, 'agregar_genero.html')

@login_required
def crear_genero(request):
    print(request.POST)
    genero = Genero(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
    genero.save()
    messages.add_message(request,messages.SUCCESS,"Se agregó el género "+"'"+genero.nombre+"'"+" correctamente", extra_tags='correcto')
    return redirect('/generos/')

@login_required
def eliminar_genero(request, id_genero):
    generos = Genero.objects.all()
    genero = Genero.objects.get(id=id_genero)
    
    peliculas_asociadas = Pelicula.objects.filter(generos=genero)

    if peliculas_asociadas:
        print(id_genero)
        messages.success(request,"No se pudo eliminar el género "+"'"+genero.nombre+"'"+". Tiene peliculas asociadas." , extra_tags='error')
        return redirect('/generos/')
    
    genero.delete()
    messages.success(request,"Se eliminó el género "+"'"+genero.nombre+"'"+" correctamente", extra_tags='correcto')
    return redirect('/generos/')

@login_required
def get_genero_id(request, id_genero):
    genero = Genero.objects.get(id=id_genero)
    return render(request, 'editar_genero.html', {"genero_obj": genero})

@login_required
def actualizar_genero(request, id_genero):
    generoActual = Genero.objects.get(id=id_genero)
    nomActual = generoActual.nombre
    desActual = generoActual.descripcion
    
    nom = request.POST.get('nombre')
    des = request.POST.get('descripcion')

    if nomActual == nom:
        if desActual == des:
            messages.success(request,"No se realizó ningún cambio al género "+"'"+nomActual+"'", extra_tags='error')
            url = reverse('generos:get_genero', args=[id_genero])
            return redirect(url)    
        
    gen = Genero(
        id = id_genero,
        nombre =  nom,
        descripcion =  des,
    )

    gen.save()
    messages.success(request,"Se modificó el género "+"'"+gen.nombre+"'"+" correctamente", extra_tags='correcto')
    url = reverse('generos:get_genero', args=[id_genero])
    return redirect(url)



