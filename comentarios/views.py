from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import ComentarioForm, ComentarioFormEditado
from .models import Comentario, Categoria
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from . import models, forms

# Create your views here.
class homeComentarios(ListView):
    model = Comentario
    template_name = 'comentarios/home.html'

#def home(request):
    #return render(request, 'home.html')

def comentarios(request):
    comentario = Comentario.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentario})


class nuevoComentario(CreateView):
    model = Comentario
    template_name = 'comentarios/nuevo_comentario.html'
    form_class = ComentarioForm
    success_url = reverse_lazy('comentarios:home')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

def modificar_comentario(request,pk):
    comenta = get_object_or_404(Comentario,pk=pk)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        form = ComentarioFormEditado(request.POST, request.FILES, instance=comentarios)
        if form.is_valid():
            form.save()
            return redirect('comentarios:home')
    else:
        form = ComentarioFormEditado(instance=comentarios)

    return render(request, 'comentarios/actualizar_comentario.html', {'form': form, 'comentario': comentarios, 'categorias': categorias})
    
def detalle_comentario(request, pk):
    contexto = {}
    listaComentarios = Comentario.objects.get(pk = pk)
    contexto['comentario'] = listaComentarios
    return render(request, 'noticias/detalle_comentario.html', contexto)

class Borrar_noticia(DeleteView):
    model = Comentario
    success_url = reverse_lazy('comentarios:home')

