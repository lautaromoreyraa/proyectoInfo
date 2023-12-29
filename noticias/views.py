from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .forms import NoticiaForm
from .models import Noticia
from comentarios.models import Comentario
from django.core.mail import send_mail
from .forms import CustomUserCreationForm

def home(request):
    ultimas_noticias = Noticia.objects.order_by('-fecha')[:3]
    return render(request, 'home.html', {'ultimas_noticias': ultimas_noticias})


def singup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'singup.html', {'form': form})
        
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
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            nueva_noticia = form.save(commit=False)
            nueva_noticia.user = request.user
            # Guardar la imagen asociada a la noticia
            if 'imagen' in request.FILES:
                nueva_noticia.imagen = request.FILES['imagen']
            nueva_noticia.save()
            return redirect('noticias')
        else:
            # Manejar el caso cuando el formulario no es válido
            return render(request, 'crear_noticia.html', {'form': form, 'error': 'Ingresa datos válidos'})
    else:
        form = NoticiaForm()
    return render(request, 'crear_noticia.html', {'form': form})

def noticia_editar(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk, user=request.user)

    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias')
    else:
        form = NoticiaForm(instance=noticia)

    return render(request, 'noticia_editar.html', {'noticia': noticia, 'form': form})
         
def borrar_noticia(request, pk):
    noticia = get_object_or_404(Noticia, pk= pk, user= request.user)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias')

def noticia_detalles(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    comentarios = Comentario.objects.filter(noticia=noticia)

    ctx = {'noticia': noticia, 'comentarios': comentarios}
    return render(request, 'noticia_detalles.html', ctx)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        send_mail(
            f'Mensaje de {name}',
            f'Email: {email}\nTeléfono: {phone}\n\nMensaje: {message}',
            email,  # Desde
            ['lautaromoreyra144@gmail.com'],  # A
            fail_silently=False,
        )
        return render(request, 'contact.html', {'success': True})  # Puedes enviar una confirmación

    return render(request, 'contact.html')  # Si es un GET, solo muestra la página de contacto
