from django import forms
from .models import Comentario

class ComentarioForm(forms.Form):
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea(attrs={'rows': 3}))


class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)