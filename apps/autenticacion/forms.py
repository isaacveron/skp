from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField, UserChangeForm


class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'telefono', 'direccion', 'observacion')

class UsuarioModForm(forms.ModelForm):
    
    username = forms.RegexField(
        label=("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href= \"password/\">this form</a>."))
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'telefono', 'direccion', 'observacion']

    def __init__(self, *args, **kwargs):
            super(UsuarioModForm, self).__init__(*args, **kwargs)
            f = self.fields.get('user_permissions', None)
            if f is not None:
                f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
            # Regardless of what the user provides, return the initial value.
            # This is done here, rather than on the field, because the
            # field does not have access to the initial value
            return self.initial["password"]

class RolForm(forms.ModelForm):
    """
    Formulario para el la creacion de roles
    Hereda de forms.ModelForm y utiliza la clase Group para
    """
    class Meta:
        model = Group
        exclude = ['Usuario']
