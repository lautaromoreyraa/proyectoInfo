from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import NoticiaForm
from .models import Noticia


def home(request):
    return render(request, 'home.html')

def singup(request):
    if request.method == 'GET' :
        return render(request, 'singup.html',{
        'form' : UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('noticias')
            except IntegrityError:
                return render(request, 'singup.html',{
                'form' : UserCreationForm,
                "error": 'El usuario ya existe'
                })
        return render(request, 'singup.html',{
                'form' : UserCreationForm,
                "error": 'Las contraseñas no coinciden'
                })
        
def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def abrir_sesion(request):
    if request.method == 'GET':
        return render(request, 'singin.html',{
            'form': AuthenticationForm
        })
    else: 
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'singin.html',{
            'form': AuthenticationForm,
            "error": 'Usuario o contraseña incorrecto'
        })
        else:
            login(request, user)
            return redirect ('noticias')

def crear_noticia(request):
    
    if request.method == 'GET':
        return render(request, 'crear_noticia.html',{
            'form': NoticiaForm
        })
    else:
        try:  
            form = NoticiaForm(request.POST)
            nueva_noticia = form.save(commit=False)
            nueva_noticia.user = request.user
            nueva_noticia.save()
            return redirect('noticias')
        except ValueError:
            return render(request, 'crear_noticia.html',{
                'form': NoticiaForm,
                "error": 'Ingresa datos validos'
            })

def noticia_detalles(request, noticia_id):
    if request.method == 'GET':
        noticia = get_object_or_404(Noticia, pk=noticia_id, user=request.user)
        form = NoticiaForm(instance=noticia)
        return render(request, 'noticia_detalles.html',{'noticia': noticia, 'form': form})
    else:
        try:
            noticia = get_object_or_404(Noticia, pk=noticia_id, user=request.user)
            NoticiaForm(request.POST, instance=noticia)
            form.save()
            return redirect ('noticias')
        except ValueError:
            return render(request, 'noticia_detalles.html',{'noticia': noticia, 'form': form, 'error': "Error al actualizar la noticia"})