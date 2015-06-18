from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField()

# django imports
from django import forms
from django.contrib.admin.forms import forms as adminforms

# third party imports
from db_file_storage.form_widgets import DBClearableFileInput, DBAdminClearableFileInput

# project imports
from apps.archivos.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['estado']
        widgets = {
            'docfile': DBClearableFileInput,
        }


class DocumentAdminForm(adminforms.ModelForm):
    class Meta:
        model = Document
        exclude = []
        widgets = {
            'docfile': DBAdminClearableFileInput,
        }
