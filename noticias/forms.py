from django import forms
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError("Los campos de contraseña son obligatorios.")

        return cleaned_data

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
