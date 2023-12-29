from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from noticias.models import Noticia
from .models import Comentario
from .forms import ComentarioForm, Form_Modificacion
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

@login_required
def agregar_comentario(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['comentario']
            usuario = request.user
            Comentario.objects.create(texto=texto, usuario=usuario, noticia=noticia)
            return HttpResponseRedirect(reverse_lazy('noticia_detalles', kwargs={'pk': pk}))
    else:
        form = ComentarioForm()

    return render(request, 'noticias_ver.html', {'form': form, 'noticia': noticia})


@login_required
def borrar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)
    if request.user == comentario.usuario:
        comentario.delete()
    return redirect('noticia_detalles', pk=comentario.noticia.pk)


@login_required
def modificar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, pk=comentario_id)

    if request.method == 'POST':
        print(request.POST)  
        form = Form_Modificacion(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('noticia_detalles', pk=comentario.noticia.pk)
    else:
        form = Form_Modificacion(instance=comentario)

    return render(request, 'modificar.html', {'form': form})

