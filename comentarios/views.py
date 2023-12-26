from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import ComentarioForm
from .models import Comentario

# Create your views here.

def home(request):
    return render(request, 'home.html')


def comentarios(request):
    comentario = Comentario.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentario})

def nuevo_comentario(request):
    if request.method == 'GET':
        return render(request, 'nuevo_comentario.html', {
            'form': ComentarioForm
        })
    else:
        try:
            form = ComentarioForm(request.POST)
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.user = request.user
            nuevo_comentario.save()
            return redirect('comentarios')
        
        except ValueError:
            return render(request, 'nuevo_comentario.html',{
                'form': ComentarioForm,
                "error": 'Ingresa datos validos'
            })
