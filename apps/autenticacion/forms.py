from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForms (forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))

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
