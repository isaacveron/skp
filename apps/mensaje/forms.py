from django.forms import ModelForm
from django import forms
from apps.usuario.models import User
from apps.mensaje.models import Mensaje

class MensajeForm(ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    class Meta:
        model = Mensaje
        exclude = ['Usuario_que_envio']
    
    