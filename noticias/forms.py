from django import forms
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'descripcion', 'imagen']  # Agrega 'imagen' a los campos del formulario
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'})  # Widget para el campo de imagen
        }


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Personalizar los mensajes de error
        self.fields['password1'].error_messages = {
            'password_too_short': 'La contraseña es demasiado corta.',
            'password_entirely_numeric': 'La contraseña no puede ser completamente numérica.',
            'password_common_sequences': 'La contraseña es demasiado común.',
            'password_too_similar': 'La contraseña es demasiado similar a la información personal.',
        }

        self.fields['password2'].error_messages = {
            'password_mismatch': 'Las contraseñas no coinciden.',
        }
