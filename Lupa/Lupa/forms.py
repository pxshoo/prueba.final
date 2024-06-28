from django import forms
from .models import usuario

class RegistroForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['username', 'password', 'email']  # Ajusta los campos según tu modelo
