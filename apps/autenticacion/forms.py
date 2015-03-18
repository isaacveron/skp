from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForms (forms.Form):
    """ Atributos Usuario y Clave del Formulario del login
        este formulario es usado para ser enviado al template html
        encargado de tomar los datos de autenticacion.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de login
        @author: Marcelo Denis
        
    """
    Usuario = forms.CharField(widget=forms.TextInput())
    Clave = forms.CharField(widget=forms.PasswordInput(render_value=False))

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True)
	
    class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
	    def save(self, commit=True):
		    user = super(FormularioRegistro, self).save(commit=False)
		    user.email = self.cleaned_data['email']

		    if commit:
			    user.save()

		return user